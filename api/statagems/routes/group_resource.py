
import logging
from flask_restful import Resource
from flask_jwt_extended.utils import get_jwt_identity
from flask import request, make_response
from sqlalchemy.orm import load_only
from ..helpers.group_helper import create_group
from ..extensions import db
from ..models.player import Player
from ..models.group import Group
from ..models.group_player import GroupPlayer
from ..schemas.group_schemas import GroupSchema

class GroupsApi(Resource): # /api/groups  
    def get(self): # get groups for specific player
        player = get_jwt_identity()
        pid = player['id']
        
        groups = db.session.query(Group).join(Group._members).filter(GroupPlayer.player_id == pid)
  
        return GroupSchema(many=True).dump(groups)

    def post(self): # add new group
        try:
            data = request.get_json()
            player = get_jwt_identity()
            pid = player['id'] 

            create_group(pid, data)

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