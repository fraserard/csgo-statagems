from typing import TypeAlias
import strawberry

from app.api.common.interfaces import ExpectedError
from app import models, db
from app.api.matches.input import AddMatchInput


@strawberry.type()
class MatchError(ExpectedError):
    pass


@strawberry.type
class PlayerNotFound(MatchError):
    message: str = "Could not find Player(s) with supplied Id(s)."


@strawberry.type
class MapNotFound(MatchError):
    message: str = "Could not find Map with supplied Id."


@strawberry.type
class DuplicatePlayers(MatchError):
    message: str = "Duplicate Player Ids supplied. All Ids must be unique."


@strawberry.type
class DuplicateStartSide(MatchError):
    message: str = (
        "Duplicate Start Side supplied. Each Team's Start Side must be different."
    )


@strawberry.type
class CaptainNotOnTeam(MatchError):
    message: str = "Captain is not playing in this Team/Match. Captains must be on their respective Team."


@strawberry.type
class CaptainMissing(MatchError):
    message: str = "Only one Captain set. Both Captains must be set or null."


@strawberry.type
class ScoreRulesInvalid(MatchError):
    message: str = "Invalid RoundsWon set. If tie both Team's RoundsWon must be 15. OR One Team's RoundsWon must be at least 16, and then multiples of 3. Must win by 2 Rounds. RoundsWon cannot be negative."


@strawberry.type
class NoPermission(MatchError):
    message: str = "You do not have permission to do that!"


AddMatchErrors: TypeAlias = strawberry.union(
    "AddMatchErrors",
    (
        PlayerNotFound,
        MapNotFound,
        DuplicatePlayers,
        CaptainNotOnTeam,
        CaptainMissing,
        ScoreRulesInvalid,
        DuplicateStartSide,
    ),
)


def add_match_validation(match_data: AddMatchInput) -> list[AddMatchErrors]:

    errors: list[AddMatchErrors] = []

    if invalid_score(
        team1_rounds_won=match_data.team1.rounds_won,
        team2_rounds_won=match_data.team2.rounds_won,
        max_rounds=match_data.MAX_ROUNDS,
        overtime_max_rounds=match_data.OVERTIME_MAX_ROUNDS,
    ):

        errors.append(ScoreRulesInvalid())

    if match_data.team1.start_side == match_data.team2.start_side:
        errors.append(DuplicateStartSide())

    if (
        match_data.team1.captain_id is None and match_data.team2.captain_id is not None
    ) or (
        match_data.team2.captain_id is None and match_data.team1.captain_id is not None
    ):
        errors.append(CaptainMissing())

    team1_player_ids = [
        player.player_id
        for player in [
            match_data.team1.player1,
            match_data.team1.player2,
            match_data.team1.player3,
            match_data.team1.player4,
            match_data.team1.player5,
        ]
    ]

    team2_player_ids = [
        player.player_id
        for player in [
            match_data.team2.player1,
            match_data.team2.player2,
            match_data.team2.player3,
            match_data.team2.player4,
            match_data.team2.player5,
        ]
    ]

    if (
        match_data.team1.captain_id not in team1_player_ids
        and match_data.team1.captain_id is not None
    ):
        errors.append(CaptainNotOnTeam())

    if (
        match_data.team2.captain_id not in team2_player_ids
        and match_data.team2.captain_id is not None
    ):
        errors.append(CaptainNotOnTeam())

    player_ids = team1_player_ids + team2_player_ids

    if duplicate_players(
        player_ids=player_ids, players_in_match_amount=match_data.PLAYER_COUNT
    ):
        errors.append(DuplicatePlayers())

    # if there are already errors - return early to avoid calling db
    if len(errors) > 0:
        return errors

    if db.session.query(models.Map.id).filter_by(id=match_data.map_id).scalar() is None:
        errors.append(MapNotFound())

    existing_players: list[int] = db.session.query(models.Player.id).filter(models.Player.id.in_(player_ids)).all()  # type: ignore (sqlalchemy in_)
    if len(existing_players) != len(player_ids):
        errors.append(PlayerNotFound())

    return errors


def invalid_score(
    team1_rounds_won: int,
    team2_rounds_won: int,
    max_rounds: int,
    overtime_max_rounds: int,
) -> bool:
    """Checks if scoreline is valid. max_rounds+1 to win. must win by 2."""

    # descending: [winner, loser], eg. [16, 8]
    score = sorted([team1_rounds_won, team2_rounds_won], reverse=True)

    # Tie: eg. [15, 15]. Valid score: exception to regular scoring rules
    if score[0] == max_rounds and score[1] == max_rounds:
        return False

    # cannot be negative
    if score[0] < 0 or score[1] < 0:
        return True

    # score cannot be less than max_rounds + 1
    if score[0] < (max_rounds + 1):
        return True

    # cannot play more rounds than there are in a game
    if (score[0] > (max_rounds + 1)) and score[1] < max_rounds:
        return True

    # Must win by 2 rounds
    if (score[0] - score[1]) < 2:
        return True

    # Overtime: eg. [19, 17]
    if score[0] > max_rounds and score[1] > max_rounds:
        # must win Overtime by overtime_max_rounds + 1
        if (score[0] - score[1]) - overtime_max_rounds != 1:
            return True

    # Valid score
    return False


def duplicate_players(player_ids: list[int], players_in_match_amount: int) -> bool:
    """Checks if there are the correct amount of unique Player ids."""

    if len({*player_ids}) < players_in_match_amount:
        return True
    return False
