import logging
from flask_restful import Resource
from flask_jwt_extended.utils import get_jwt_identity
from flask import request, make_response
from ..helpers.group_helper import create_group
from ..extensions import db
from ..models.player import Player

class GroupsApi(Resource): # /api/groups   
    def get(self): # get groups for specific player
        player = get_jwt_identity()
        groups = Player.query.get(player['id']).load_only(Player.groups)
        return NotImplemented

    def post(self): # add new group
        try:
            data = request.get_json()
            player_jwt = get_jwt_identity()
            create_group(player_jwt['id'], data)
            db.session.commit()
        except Exception as e:
            logging.exception(e)
            return {'msg': 'error'}, 400
        except BaseException as e:
            logging.exception(e)
            return {'msg': 'error'}, 400
        
        return {'msg': 'success'}, 201

class GroupApi(Resource): # /api/groups/<id>
    def get(self): # get group by id
        
        return NotImplemented

    def put(self): # update group
        
        return NotImplemented