import datetime
from marshmallow import fields
from ..extensions import ma
from ..models import Group

class GroupSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Group
    id = ma.auto_field()
    creator_id = ma.auto_field()
    group_name = ma.auto_field()
    description = ma.auto_field()
    matches = ma.auto_field()
    members = ma.auto_field()
    created_at = ma.auto_field()