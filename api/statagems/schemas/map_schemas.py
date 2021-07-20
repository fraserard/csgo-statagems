from ..extensions import ma
from ..models import Map

class MapSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Map
        include_fk = True
        include_relationships = True    

map_schema = MapSchema()
maps_schema = MapSchema(many=True)
