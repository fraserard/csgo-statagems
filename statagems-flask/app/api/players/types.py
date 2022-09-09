from datetime import datetime
from typing import NewType

import strawberry
from app import models
from app.api.common.interfaces import Node, PlayerAggregates, TeamAggregates
from app.api.common.types.avatar_url import (
    AVATAR_URL,
    DEFAULT_AVATAR_URL,
    EMPTY_AVATAR_HASH,
    AvatarUrl,
)
from app.api.matches.types import Match
from app.api.permissions import RoleType
from app.services import players
from typing_extensions import Self

SteamID = strawberry.scalar(
    NewType("SteamID", str),
    description="64 bit SteamID. Like: 7656xxxxxxxxxxxxx",
    serialize=lambda v: v,
    parse_value=lambda v: v,
)


@strawberry.type
class LoggedInUser(Node):
    steam_username: str
    username: str
    role: RoleType

    steam_avatar_hash: strawberry.Private[str]

    @strawberry.field
    def avatar_url(self) -> str:
        if self.steam_avatar_hash == EMPTY_AVATAR_HASH:
            return f"{DEFAULT_AVATAR_URL}_medium.jpg"
        return f"{AVATAR_URL}{self.steam_avatar_hash}_medium.jpg"

    @strawberry.field
    def roles(self) -> list[RoleType]:
        if self.role == RoleType.ADMIN:
            return [RoleType.ADMIN, RoleType.MOD, RoleType.REF, RoleType.USER]
        if self.role == RoleType.MOD:
            return [RoleType.MOD, RoleType.REF, RoleType.USER]
        if self.role == RoleType.REF:
            return [RoleType.REF, RoleType.USER]
        return [RoleType.USER]

    @classmethod
    def marshal(cls, model: models.Player) -> Self:
        return cls(
            id=strawberry.ID(str(model.id)),
            username=model.username,
            steam_username=model.steam_username,
            steam_avatar_hash=model.steam_avatar_hash,
            role=RoleType(model.role.value),
        )


@strawberry.type
class Player(Node, PlayerAggregates, TeamAggregates):
    username: str
    steam_id: SteamID
    steam_username: str
    steam_real_name: str | None
    role: RoleType
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
        return AvatarUrl(steam_avatar_hash=self.steam_avatar_hash)

    @strawberry.field
    def matches(self) -> list["Match"] | None:
        matches_data: list["models.Match"] = players.get_matches(int(self.id))
        return [Match.marshal(match_data) for match_data in matches_data]

    @classmethod
    def marshal(cls, model: "models.Player") -> Self:
        return cls(
            id=strawberry.ID(str(model.id)),
            username=model.username,
            steam_id=SteamID(model.steam_id),
            steam_username=model.steam_username,
            steam_real_name=model.steam_real_name,
            steam_avatar_hash=model.steam_avatar_hash,
            role=RoleType(model.role.name),
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

    # teams: List['Team'] # get teams for player
