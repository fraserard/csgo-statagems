from flask.views import MethodView

from app.models import Map
from app.api.schemas import MapSchema

class MapsAPI(MethodView): # /api/v1/maps
    def get(self):
        maps = Map.query.all()
        map_schema = MapSchema(many=True)  
       
        return map_schema.jsonify(maps)