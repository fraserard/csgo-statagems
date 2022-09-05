from enum import Enum
from typing import Any

import strawberry
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import JWTExtendedException
from jwt import ExpiredSignatureError
from strawberry.permission import BasePermission
from strawberry.types import Info


@strawberry.enum(name="Role")
class RoleType(Enum):
    ADMIN = "ADMIN"
    MOD = "MOD"
    REF = "REF"
    USER = "USER"
    REMOVED = "REMOVED"


def get_user() -> tuple[int, RoleType] | tuple[None, None]:
    try:
        jwt = verify_jwt_in_request(optional=True)
        if jwt is None:
            return None, None

        jwt_header, jwt_data = jwt

    except (JWTExtendedException, ExpiredSignatureError):
        return None, None

    jwt_data = jwt_data["sub"]
    role = RoleType(jwt_data["role"])
    player_id = int(jwt_data["player_id"])
    
    return player_id, role


class Permission(BasePermission):
    code = "PERMISSION"
    message = "Not permitted."

class IsPlayer(Permission):
    def has_permission(self, source: Any, info: Info, **kwargs) -> bool:
        _, role = get_user()
        if role is None:
            return False

        if RoleType(role) in [RoleType.USER, RoleType.REF, RoleType.ADMIN, RoleType.MOD]:
            return True

        return False
    
class IsRef(Permission):
    def has_permission(self, source: Any, info: Info, **kwargs) -> bool:
        _, role = get_user()
        if role is None:
            return False

        if RoleType(role) in [RoleType.REF, RoleType.ADMIN, RoleType.MOD]:
            return True

        return False


class IsMod(Permission):
    def has_permission(self, source: Any, info: Info, **kwargs) -> bool:
        _, role = get_user()
        if role is None:
            return False

        if RoleType(role) in [RoleType.MOD, RoleType.ADMIN]:
            return True

        return False


class IsAdmin(Permission):
    def has_permission(self, source: Any, info: Info, **kwargs) -> bool:
        _, role = get_user()
        if role is None:
            return False

        if RoleType(role) in [RoleType.ADMIN]:
            return True

        return False
