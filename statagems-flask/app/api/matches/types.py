from datetime import datetime
from enum import Enum

import strawberry
from typing_extensions import Self

from app import models
from app.api.common.interfaces import Node
from app.api.common.types.avatar_url import AvatarUrl
from app.api.maps.types import Map


@strawberry.enum
class TeamSide(Enum):
    CT = "CT"
    T = "T"


@strawberry.enum()
class Outcome(Enum):
    WON = "WON"
    LOST = "LOST"
    TIED = "TIED"


@strawberry.type()
class Match(Node):
    date_played: datetime
    map: Map
    teams: list["MatchTeam"]

    @strawberry.field(
        description="formatted like 'winner_score-loser_score' ex. 16-8, 16-14"
    )
    def score(self) -> str:
        return f"{self.teams[0].rounds_won}-{self.teams[1].rounds_won}"

    @classmethod
    def marshal(cls, model: models.Match) -> Self:
        # sort team by rounds won. index 0 is winner. index 1 is loser.
        # if tie, sort is irrelevant
        model.teams.sort(key=lambda team: team.rounds_won, reverse=True)

        winning_team = model.teams[0]
        losing_team = model.teams[1]
        teams = [
            MatchTeam.marshal(winning_team, losing_team.rounds_won),
            MatchTeam.marshal(losing_team, winning_team.rounds_won),
        ]

        return cls(
            id=strawberry.ID(str(model.id)),
            map=Map.marshal(model.map),
            date_played=model.date_played,
            teams=teams,
        )


@strawberry.type
class MatchTeam(Node):
    match_id: int
    team_id: int
    start_side: TeamSide
    rounds_won: int
    rounds_lost: int
    match_players: list["MatchPlayer"]
    captain_id: int | None
    # captain: "Player" | None

    @strawberry.field
    def outcome(self) -> Outcome:
        if self.rounds_won < self.rounds_lost:
            return Outcome.LOST
        if self.rounds_won > self.rounds_lost:
            return Outcome.WON
        return Outcome.TIED

    @classmethod
    def marshal(cls, model: "models.MatchTeam", rounds_lost: int) -> Self:
        return cls(
            id=strawberry.ID(f"{model.match_id}.{model.team_id}"),
            match_id=model.match_id,
            team_id=model.team_id,
            start_side=model.start_side.value,
            rounds_won=model.rounds_won,
            rounds_lost=rounds_lost,
            captain_id=model.captain_id,
            match_players=[
                MatchPlayer.marshal(player_data) for player_data in model.players
            ],
        )


@strawberry.type
class MatchPlayer(Node):
    player_id: int
    kills: int
    deaths: int
    assists: int
    adr: int | None
    score: int | None
    mvps: int | None
    steam_username: str

    steam_avatar_hash: strawberry.Private[str]

    @strawberry.field
    def avatar(self) -> AvatarUrl:
        return AvatarUrl(strawberry.ID(self.steam_avatar_hash))

    # player: 'Player'
    # is accessing user? flag to display if this record relates to player making request

    @classmethod
    def marshal(cls, model: "models.MatchPlayer") -> Self:
        return cls(
            id=strawberry.ID(f'{model.match_id}.{model.player_id}'),
            player_id=model.player_id,
            kills=model.kills,
            deaths=model.deaths,
            assists=model.assists,
            adr=model.adr,
            score=model.score,
            mvps=model.mvps,
            steam_username=model.steam_username,
            steam_avatar_hash=model.steam_avatar_hash,
        )
