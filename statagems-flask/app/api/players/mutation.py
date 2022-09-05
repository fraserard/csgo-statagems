from enum import Enum
from typing import Generic

import strawberry
from flask_jwt_extended import unset_access_cookies
from strawberry.types.info import ContextType, Info, RootValueType

from app import db, models
from app.api.permissions import IsMod, IsPlayer, RoleType, get_user
from app.api.players.types import Player


@strawberry.enum()
class UpdatePlayerInputRole(Enum):
    MOD = "MOD"
    REF = "REF"
    USER = "USER"
    REMOVED = "REMOVED"


@strawberry.input
class UpdatePlayerInput:
    player_id: int
    username: str
    role: UpdatePlayerInputRole


@strawberry.type
class Mutation:
    @strawberry.mutation
    def logout(self, info: Info) -> None:
        unset_access_cookies(info.context["response"]) 
        return None

    @strawberry.mutation(permission_classes=[IsMod])
    def add_player(self, steam_id: str) -> Player:
        player = models.Player.whitelist(steam_ids=[steam_id])[0]
        db.session.commit()
        # Player not found
        # Player already on whitelist
        return Player.marshal(player)

    @strawberry.mutation(permission_classes=[IsMod])
    def update_player(self, player_data: UpdatePlayerInput) -> Player:
        player: models.Player = (
            db.session.query(models.Player).filter_by(id=player_data.player_id).scalar()
        )
        user_id, user_role = get_user()
        if (user_role != RoleType.ADMIN) and (player.role == models.PlayerRoles.ADMIN):
            Exception("Must be Admin to update Admin.")

        player.username = player_data.username
        player.role = models.PlayerRoles(player_data.role.value)

        db.session.commit()
        return Player.marshal(player)

    @strawberry.mutation(permission_classes=[IsPlayer])
    def update_username(self, username: str) -> Player:
        ...
