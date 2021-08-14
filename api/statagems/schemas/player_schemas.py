from .. import ma
from ..models.player import Player

class PlayerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Player
    id = ma.auto_field()
    steam_id = ma.auto_field()
    username = ma.auto_field()
    name = ma.auto_field()
    preferred_username = ma.auto_field()
    avatar_hash = ma.auto_field()
    acct_type = ma.auto_field()

class PlayerSteamSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Player
        load_instance = True
        include_relationships = True
    steamid = Player.steam_id
    personaname = Player.username
    realname = Player.name
    avatarhash = Player.avatar_hash

# class PlayerIdSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = Player
#     id = ma.auto_field()
       
player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)

#player_steam_schema = PlayerSchema(only=["steam_id", "username", "name", "avatar_hash"], load_instance = True)
player_steam_schema = PlayerSteamSchema()

# # only returns player ids for getStaticPaths
players_id_schema = PlayerSchema(many=True, only=["id"]) 