from datetime import datetime

import strawberry
from app import db
from app.api.matches.input import AddMatchInput

from app.services import matches
from app.api.matches.types import Match
from app.api.matches.validation import AddMatchErrors, add_match_validation


@strawberry.type
class AddMatchPayload:
    match: Match | None
    errors: list[AddMatchErrors]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_match(self, match_data: AddMatchInput) -> AddMatchPayload:

        # validate user permissions
        # validate input

        errors = add_match_validation(match_data)
        if errors:
            return AddMatchPayload(match=None, errors=errors)

        # new_teams: list[matches.NewMatchTeam] = []
        # for team_data in [match_data.team1, match_data.team2]:

        #     players_data = [
        #         team_data.player1,
        #         team_data.player2,
        #         team_data.player3,
        #         team_data.player4,
        #         team_data.player5,
        #     ]

        #     new_players = [
        #         matches.NewMatchPlayer(
        #             player_id=player_data.player_id,
        #             kills=player_data.kills,
        #             assists=player_data.assists,
        #             deaths=player_data.deaths,
        #         )
        #         for player_data in players_data
        #     ]

        #     new_team = matches.NewMatchTeam(
        #         start_side=team_data.start_side.value,
        #         rounds_won=team_data.rounds_won,
        #         captain_id=team_data.captain_id,
        #         players=new_players,
        #     )
        #     new_teams.append(new_team)

        # new_match = matches.NewMatch(
        #     map_id=match_data.map_id,
        #     date_played=datetime.utcnow(),
        #     team1=new_teams[0],
        #     team2=new_teams[1],
        # )
  

        setattr(match_data, "date_played", datetime.utcnow())
             
        setattr(match_data.team1, "rounds_lost", match_data.team2.rounds_won)
        setattr(match_data.team2, "rounds_lost", match_data.team1.rounds_won)

        for team in [match_data.team1, match_data.team2]:
            setattr(team, "start_side", team.start_side.value)
            setattr(
                team,
                "players",
                [team.player1, team.player2, team.player3, team.player4, team.player5],
            )
            

        match = matches.add_match(new_match=match_data)  # WHY

        return AddMatchPayload(match=Match.marshal(match), errors=errors)


# removeMatch
# editMatch
