from .. import ma
from ..models.player import Player

class PlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Player
        include_fk = True
        include_relationships = True

player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)