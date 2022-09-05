import strawberry

from app import models
from app.api.common.interfaces import Node


@strawberry.type
class Map(Node):
    filename: str
    map_name: str
    active_duty: bool
    removed: bool

    @classmethod
    def marshal(cls, model: models.Map) -> "Map":
        return cls(
            id=strawberry.ID(str(model.id)),
            filename=model.filename,
            map_name=model.map_name,
            active_duty=model.is_active_duty,
            removed=model.is_removed or False,
        )

    
