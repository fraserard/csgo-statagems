from email import message
from typing import TypeAlias

import strawberry
from strawberry.types import Info

from app import db, models
from app.api.common.interfaces import ExpectedError
from app.api.maps.types import Map
from app.api.permissions import IsMod


@strawberry.input
class AddMapInput:
    filename: str
    map_name: str
    active_duty: bool
    removed: bool


@strawberry.input
class UpdateMapInput:
    id: strawberry.ID
    filename: str
    map_name: str
    active_duty: bool
    removed: bool


@strawberry.type
class FilenameTooLong(ExpectedError):
    message: str = "Filename must be under 32 characters in length"


@strawberry.type
class MapNameTooLong(ExpectedError):
    message: str = "Map name must be under 32 characters in length"


AddMapErrors: TypeAlias = strawberry.union(
    "AddMapErrors",
    (
        FilenameTooLong,
        MapNameTooLong,
    ),
)


@strawberry.type
class AddMapPayload:
    map: Map | None
    errors: list[AddMapErrors]


UpdateMapErrors: TypeAlias = strawberry.union(
    "UpdateMapErrors",
    (
        FilenameTooLong,
        MapNameTooLong,
    ),
)


@strawberry.type
class UpdateMapPayload:
    map: Map | None
    errors: list[UpdateMapErrors]


@strawberry.type
class Mutation:
    @strawberry.mutation(permission_classes=[IsMod])
    def add_map(self, map_data: AddMapInput) -> AddMapPayload:
        errors: list[AddMapErrors] = []
        if len(map_data.filename) > 32:
            errors.append(FilenameTooLong())
        if len(map_data.map_name) > 32:
            errors.append(MapNameTooLong())
        if errors:
            return AddMapPayload(map=None, errors=errors)

        map = models.Map(
            filename=map_data.filename,
            map_name=map_data.map_name,
            is_active_duty=map_data.active_duty,
            is_removed=map_data.removed,
        )

        db.session.add(map)
        db.session.commit()
        return AddMapPayload(map=Map.marshal(map), errors=errors)

    @strawberry.mutation(permission_classes=[IsMod])
    def update_map(self, map_data: UpdateMapInput) -> UpdateMapPayload:
        errors: list[UpdateMapErrors] = []
        if len(map_data.filename) > 32:
            errors.append(FilenameTooLong())
        if len(map_data.map_name) > 32:
            errors.append(MapNameTooLong())
        if errors:
            return UpdateMapPayload(map=None, errors=errors)

        map = db.session.query(models.Map).filter_by(id=map_data.id).scalar()
        map.map_name = map_data.map_name
        map.is_active_duty = map_data.active_duty
        map.is_removed = map_data.removed

        db.session.commit()
        return UpdateMapPayload(map=Map.marshal(map), errors=errors)
