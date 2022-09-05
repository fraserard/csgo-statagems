import strawberry

from app import db, models
from app.api.maps.types import Map


@strawberry.type
class Query:
    @strawberry.field(description="Get a list of all maps. (Incl. removed maps)")
    def maps(self) -> list["Map"]:
        maps_data: list["models.Map"] = models.Map.query.all()
        return [Map.marshal(map_data) for map_data in maps_data]

    @strawberry.field(description="Get a list of all playable maps.")
    def playable_maps(self) -> list["Map"]:
        maps_data: list["models.Map"] = (
            db.session.query(models.Map).filter_by(is_removed=False or None).all()
        )
        return [Map.marshal(map_data) for map_data in maps_data]
