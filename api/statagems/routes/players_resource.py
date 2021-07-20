from flask import request
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource


from ..extensions import db
from ..models.player import Player 
from ..schemas.player_schemas import players_schema, player_schema

class PlayersApi(Resource): # /api/players
    @jwt_required()
    def get(self): # get all players
        players = Player.query.all()
        return players_schema.dump(players)
    @jwt_required()    
    def post(self): # add a player
        data = request.get_json()
        new_player = Player(
            steam_id = data['steam_id'],
            username = data['username'],
            preferred_username = data['preferred_username'],
            name = data['name'],
            profile_pic_url = data['profile_pic_url'])
        db.session.add(new_player)
        db.session.commit()
        return {"msg": "success"}

class PlayerApi(Resource): # /api/players/<id>
    @jwt_required()
    def get(self, id): # get a player by id
        player = Player.query.get_or_404(id)
        return player_schema.dump(player)
    @jwt_required()
    def put(self, id): # update player by id
        data = request.get_json()
        player = Player.query.get(id)
        if player is None:
            return {"msg": "error",
                    "reason": "No player found."}
        if 'username' in data:
            player.username = data['username']
        if 'preferred_username' in data:
            player.preferred_username = data['preferred_username']
        if 'name' in data:
            player.name = data['name']
        db.session.commit()
        return {"msg": "success"}
    @jwt_required()    
    def delete(self, id): # delete a player by id
        player = Player.query.get(id)
        if player is None:
            return {"msg": "error",
                    "reason": "No player found."}
        db.session.delete(player)
        db.session.commit()
        return {"msg": "success"}
