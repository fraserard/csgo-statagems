from app import ma
from app.models import Player

class PlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Player
        include_fk = True