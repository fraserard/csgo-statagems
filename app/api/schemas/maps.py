from app import ma
from app.models import Map

class MapSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Map
        include_fk = True