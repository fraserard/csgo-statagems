from api.model import MatchPlayer, Player, Map, Match
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class PlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Player
        include_fk = True
        include_relationships = True

player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)

class MatchSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Match
        include_fk = True
        include_relationships = True

match_schema = MatchSchema()

class MatchPlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MatchPlayer
        include_fk = True
        include_relationships = True

class MapSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Map
        include_fk = True
        include_relationships = True    
    
