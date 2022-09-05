from datetime import datetime

import strawberry

from app import db
from app.api.matches.input import AddMatchInput, AddMatchTeamInput
from app.api.matches.types import Match
from app.api.matches.validation import AddMatchErrors, add_match_validation
from app.api.permissions import IsRef
from app.services import matches, teams


@strawberry.type
class AddMatchPayload:
    match: Match | None
    errors: list[AddMatchErrors]


@strawberry.type
class Mutation:
    @strawberry.mutation(permission_classes=[IsRef])
    def add_match(self, match_data: AddMatchInput) -> AddMatchPayload:
        errors = add_match_validation(match_data)
        if errors:
            return AddMatchPayload(match=None, errors=errors)

        new_match = create_new_match(match=match_data)

        match = matches.process_match(match_data=new_match)

        db.session.add(match)
        db.session.commit()

        return AddMatchPayload(match=Match.marshal(match), errors=errors)

    @strawberry.mutation(permission_classes=[IsRef])
    def remove_match(self, match_id: int) -> bool:
        # adjust statistics aggregates
        # remove match
        return NotImplemented


def create_new_match(match: AddMatchInput) -> matches.NewMatch:
    return matches.NewMatch(
        map_id=match.map_id,
        date_played=datetime.utcnow(),
        team1=create_new_match_team(
            match_team=match.team1, rounds_lost=match.team2.rounds_won
        ),
        team2=create_new_match_team(
            match_team=match.team2, rounds_lost=match.team1.rounds_won
        ),
    )


def create_new_match_team(
    match_team: AddMatchTeamInput, rounds_lost: int
) -> matches.NewMatchTeam:

    match_players = [
        player
        for player in [
            match_team.player1,
            match_team.player2,
            match_team.player3,
            match_team.player4,
            match_team.player5,
        ]
    ]

    player_ids = {player.player_id for player in match_players}

    return matches.NewMatchTeam(
        start_side=match_team.start_side.value,
        rounds_won=match_team.rounds_won,
        rounds_lost=rounds_lost,
        captain_id=match_team.captain_id,
        team_hash=teams.create_team_hash(player_ids),
        players=[
            matches.NewMatchPlayer(
                player_id=match_player.player_id,
                kills=match_player.kills,
                assists=match_player.assists,
                deaths=match_player.deaths,
            )
            for match_player in match_players
        ],
    )
