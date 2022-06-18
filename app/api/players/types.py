from datetime import datetime
from enum import Enum
from typing import NewType
from typing_extensions import Self

import strawberry
from strawberry.types import Info

from app import models
from app.api.common.interfaces import (
    TeamAggregates,
    PlayerAggregates,
    Node,
)
from app.api.common.types.avatar_url import AvatarUrl
from app.api.matches.types import Match
from app.services import players


SteamID = strawberry.scalar(
    NewType("SteamID", str),
    description="64 bit SteamID. Like: 7656xxxxxxxxxxxxx",
    serialize=lambda v: v,
    parse_value=lambda v: v,
)


@strawberry.interface
class IPlayer(Node, PlayerAggregates, TeamAggregates):
    steam_id: SteamID
    steam_username: str
    steam_real_name: str | None
    role: "Role"
    last_seen: datetime

    @strawberry.field
    def games_played(self) -> int:
        return self.games_won + self.games_lost + self.games_tied

    @strawberry.field
    def steam_profile_url(self) -> str:
        return f"https://steamcommunity.com/profiles/{self.steam_id}"

    steam_avatar_hash: strawberry.Private[str]

    @strawberry.field
    def avatar(self) -> AvatarUrl:
        return AvatarUrl(self.steam_avatar_hash)

    @classmethod
    def marshal(cls, model: "models.Player") -> Self:
        return cls(
            id=strawberry.ID(str(model.id)),
            steam_id=SteamID(model.steam_id),
            steam_username=model.steam_username,
            steam_real_name=model.steam_real_name,
            steam_avatar_hash=model.steam_avatar_hash,
            role=model.role.value,
            times_captain=model.times_captain,
            kills=model.kills,
            assists=model.assists,
            deaths=model.deaths,
            adr=model.adr,
            score=model.score,
            mvps=model.mvps,
            games_won=model.games_won,
            games_lost=model.games_lost,
            games_tied=model.games_tied,
            rounds_won=model.rounds_won,
            rounds_lost=model.rounds_lost,
            times_started_ct=model.times_started_ct,
            times_started_t=model.times_started_t,
            last_seen=model.last_seen,
        )


@strawberry.type
class Player(IPlayer):

    @strawberry.field
    def matches(self) -> list["Match"] | None:
        matches_data: list["models.Match"] = players.get_matches(int(self.id))
        return [Match.marshal(match_data) for match_data in matches_data]
    
    # teams: List['Team'] # get teams for player

@strawberry.type
class PlayerList(IPlayer):
    pass


@strawberry.enum(name="Role")
class Role(Enum):
    ADMIN = "ADMIN"
    MOD = "MOD"
    REF = "REF"
    USER = "USER"
