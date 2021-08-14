from flask import request
from flask.helpers import make_response
from flask_jwt_extended.utils import get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
import logging

from ..extensions import db
from ..models.player import Player 
from ..schemas.player_schemas import players_schema, player_schema, players_id_schema

class PlayersApi(Resource): # /api/players   
    @jwt_required(optional=True)
    def get(self): # get all players
        if get_jwt_identity():
            players = Player.query.all()
            return players_schema.dump(players)
        else: # returns id of each player for static routes. Change this to use SteamId instead?
            players = Player.query.all()
            return players_schema.dump(players)

class PlayerApi(Resource): # /api/players/<id>
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
    def delete(self, id): # delete a player by id
        player = Player.query.get(id)
        if player is None:
            return {"msg": "error",
                    "reason": "No player found."}
        db.session.delete(player)
        db.session.commit()
        return {"msg": "success"}

class PlayerSelf(Resource): # /api/me
    @jwt_required()
    def get(self):
        res = make_response()
        try:
            player = get_jwt_identity()
            return player
        except Exception as e:
            logging.exception(f'/api/me exception: {e}')
            return res, 403
        
        
