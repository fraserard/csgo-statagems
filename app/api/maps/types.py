from typing_extensions import Self

import strawberry

# from app.matches.types import Match
from app import models
from app.api.common.interfaces import Node


@strawberry.type
class Map(Node):
    filename: str
    map_name: str
    active_duty: bool

    @classmethod
    def marshal(cls, model: "models.Map") -> Self:
        return cls(
            id=strawberry.ID(str(model.id)),
            filename=model.filename,
            map_name=model.map_name,
            active_duty=model.is_active_duty,
        )

    # matches: List['Match']
