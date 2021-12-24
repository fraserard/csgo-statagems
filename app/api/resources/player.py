from flask.views import MethodView

from app.models import Player
from app.api.schemas import PlayerSchema

class PlayersAPI(MethodView): # /api/v1/players
    
    # method_decorators = [jwt_required()]
    
    def get(self):
        players = Player.query.all()
        player_schema = PlayerSchema(many=True)  
        
        return player_schema.jsonify(players)