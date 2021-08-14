from ..helpers.player_helper import new_player_by_steam_id
from flask import request
from ..extensions import db
from flask.helpers import make_response
from flask_restful import Resource
from ..models import Player
from ..schemas.player_schemas import players_schema, player_schema
import logging
from flask_restful import url_for

# TODO CREATE ADMIN ONLY JWT DECORATOR
class AdminPlayers(Resource): # /admin/players   
    def get(self): # get all players
        players = Player.query.all()
        return players_schema.dump(players)

    def post(self): # add a player by steam id
        data = request.get_json()
        try:
            new_player_by_steam_id(data['steam_id'])
        except Exception as e:
            logging.exception(e)
        except BaseException as e:
            logging.critical(f'{AdminPlayers.__name__} BaseException. {e}')
        db.session.commit()
        return {"msg": "success"}

class AdminPlayer(Resource): # /admin/players/<id>
    def get(self, id): # get a player by id
        player = Player.query.get_or_404(id)
        return player_schema.dump(player)
   
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