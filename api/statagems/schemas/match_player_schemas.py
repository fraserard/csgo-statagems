from ..extensions import ma
from ..models import MatchPlayer

class MatchPlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MatchPlayer
        include_fk = True
        include_relationships = True

match_player_schema = MatchPlayerSchema()
match_players_schema = MatchPlayerSchema(many=True)