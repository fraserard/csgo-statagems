from flask import request
from .model import db, Player
from flask_restful import Resource
from .schemas import players_schema, player_schema

def initialize_routes(api):
    api.add_resource(PlayersApi, '/api/players')
    api.add_resource(PlayerApi, '/api/players/<id>')

class PlayersApi(Resource):
    def get(self): # get all players
        players = Player.query.all()
        return players_schema.dump(players)
        
    def post(self): # add a player
        data = request.get_json()
        newPlayer = Player(
            steam_id = data['steam_id'],
            username = data['username'],
            preferred_username = data['preferred_username'],
            name = data['name'])
        db.session.add(newPlayer)
        db.session.commit()
        return {"msg": "success"}
        #return player_schema.dump(newPlayer)

class PlayerApi(Resource):
    def get(self, id): # get a player by id
        player = Player.query.get_or_404(id)
        return player_schema.dump(player)
    def put(self, id): # update player by id
        data = request.get_json()
        player = Player.query.get()
        if player is None:
            return {"msg": "error",
                    "reason": "No player found."}
        if data['username'] is not None:
            player.username = data['username']
        if data['preferred_username'] is not None:
            player.preferred_username = data['preferred_username']
        if data['name'] is not None:
            player.name = data['name']
        db.session.commit()
        return {"msg": "success"}
    def delete(self, id): # delete a player by id
        player = Player.query.get_or_404(id)
        db.session.delete(player)
        db.session.commit()
        return {"msg": "success"}
