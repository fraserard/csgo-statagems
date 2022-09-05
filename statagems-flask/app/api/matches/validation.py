from typing import TypeAlias

import strawberry

from app import db, models
from app.api.common.interfaces import ExpectedError
from app.api.matches.input import AddMatchInput


@strawberry.type
class PlayerNotFound(ExpectedError):
    message: str = "Could not find selected player(s)."


@strawberry.type
class MapNotFound(ExpectedError):
    message: str = "Could not find selected map."


@strawberry.type
class DuplicatePlayers(ExpectedError):
    message: str = "All players must be unique."


@strawberry.type
class DuplicateStartSide(ExpectedError):
    message: str = "Each team's start side must be different."


@strawberry.type
class CaptainNotOnTeam(ExpectedError):
    message: str = "Captains must be on their respective team."


@strawberry.type
class OnlyOneCaptainSet(ExpectedError):
    message: str = "Set both captains or none at all."


@strawberry.type
class ScoreRulesInvalid(ExpectedError):
    message: str = "Invalid score set. If tie both teams must have won 15 rounds. If win one team must have won at least 16 rounds. Must win by 2 Rounds."


@strawberry.type
class NoPermission(ExpectedError):
    message: str = "You do not have permission to do that!"


AddMatchErrors: TypeAlias = strawberry.union(
    "AddMatchErrors",
    (
        PlayerNotFound,
        MapNotFound,
        DuplicatePlayers,
        CaptainNotOnTeam,
        OnlyOneCaptainSet,
        ScoreRulesInvalid,
        DuplicateStartSide,
    ),
)
# TODO Add errors for impossible stats. ie. more deaths than rounds played


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
        errors.append(OnlyOneCaptainSet())

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

    round_difference = score[0] - score[1]
    # Must win by 2 rounds
    if round_difference < 2:
        return True

    # Overtime: eg. [19, 17]
    if score[0] > max_rounds and score[1] > max_rounds:
        # Winner score must be: max_rounds + n(overtime_max_rounds) + 1
        number_of_overtimes = (score[0] - max_rounds - 1) / overtime_max_rounds
        if not number_of_overtimes.is_integer():
            return True

        # must win Overtime by overtime_max_rounds + 1
        if round_difference - overtime_max_rounds not in [-1, 0, 1]:
            return True

    # Valid score
    return False


def duplicate_players(player_ids: list[int], players_in_match_amount: int) -> bool:
    """Checks if there are the correct amount of unique Player ids."""

    if len({*player_ids}) < players_in_match_amount:
        return True
    return False
