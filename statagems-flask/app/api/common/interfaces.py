from typing import Optional, TypedDict

import strawberry


@strawberry.interface
class Node:
    id: strawberry.ID


# TODO CHANGE TO TYPES,
# CHANGE REFERENCES TO USE COMPOSITION
@strawberry.interface
class PlayerAggregates:
    kills: int
    assists: int
    deaths: int
    adr: Optional[int]
    score: int
    mvps: int
    times_captain: int


@strawberry.interface
class TeamAggregates:
    games_won: int
    games_lost: int
    games_tied: int
    rounds_won: int
    rounds_lost: int
    times_started_ct: int
    times_started_t: int

    # round win percentage
    # game win percentage
    # total games played
    # times won when captain
    # captain / win ratio

@strawberry.interface
class ExpectedError:
    @strawberry.field
    def message(self) -> str:
        return f"{self.message}"
