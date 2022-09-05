from datetime import datetime

import strawberry

from app.api.matches.types import TeamSide


@strawberry.input
class AddMatchPlayerInput:
    player_id: int
    kills: int
    assists: int
    deaths: int


@strawberry.input
class AddMatchTeamInput:
    start_side: TeamSide
    rounds_won: int
    player1: AddMatchPlayerInput
    player2: AddMatchPlayerInput
    player3: AddMatchPlayerInput
    player4: AddMatchPlayerInput
    player5: AddMatchPlayerInput
    captain_id: int | None = None


@strawberry.input()
class AddMatchInput:
    map_id: int
    team1: AddMatchTeamInput
    team2: AddMatchTeamInput

    
    PLAYER_COUNT: strawberry.Private[int] = 10
    MAX_ROUNDS: strawberry.Private[int] = 15
    OVERTIME_MAX_ROUNDS: strawberry.Private[int] = 3
