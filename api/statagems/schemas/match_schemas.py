from ..extensions import ma
from ..models.match import Match

class MatchSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Match
        include_fk = True
        include_relationships = True

match_schema = MatchSchema()
matches_schema = MatchSchema(many=True)