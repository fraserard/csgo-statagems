
from statagems.schemas.player_schemas import PlayerSchema
from marshmallow import Schema, fields as f
from ..extensions import ma
from ..models import Group
class GroupSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Group
    id = ma.auto_field()
    creator_id = ma.auto_field()
    group_name = ma.auto_field()
    description = ma.auto_field()
    #matches = ma.auto_field()
    members = ma.auto_field()
    created_at = ma.auto_field()

class GroupPlayerSchema(Schema):
    group_id = f.Int()
    creator_id = f.Int()
    group_name = f.Str()
    description = f.Str()
    members = f.List(f.Nested(PlayerSchema(only=['id', 'username'])))

# GroupPlayerSchema = Schema.from_dict({
#     'group_id': f.Int(),
#     'creator_id': f.Int(),
#     'group_name': f.Str(),
#     'description': f.Str(),
#     'members' : f.List({
#         'player_id':f.Int(),
#         'username': f.Str()
#     })
# })