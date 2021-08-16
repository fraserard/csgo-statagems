
import logging
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from flask_jwt_extended.utils import get_jwt_identity
from flask import request
from ..helpers.group_helper import create_group, update_group, delete_group
from ..extensions import db
from ..models.group import Group
from ..models.group_player import GroupPlayer
from ..schemas.group_schemas import GroupSchema

class GroupsApi(Resource): # /api/groups 
    @jwt_required() 
    def get(self): # get groups for specific player
        try:
            player = get_jwt_identity()
            pid = player['id']
        
            groups = db.session.query(Group).join(Group._members).filter(GroupPlayer.player_id == pid)
        except Exception as e:
            logging.exception(e)
            return 400
        
        return GroupSchema(many=True).dump(groups), 200
    @jwt_required()
    def post(self): # add new group
        data = request.get_json(silent=True)
        if data is None: return 400
        try:
            data = request.get_json()
            player = get_jwt_identity()
            pid = player['id'] 

            create_group(creator_id=pid, group_data=data)

            db.session.commit()
        except Exception as e:
            logging.exception(e)
            return 400
        
        return 201

class GroupApi(Resource): # /api/groups/<gid>
    @jwt_required()
    def get(self, gid): # get group by groupid
        group = Group.query.get_or_404(gid)
        return GroupSchema().dump(group), 200

    @jwt_required()
    def put(self, gid): # update group by groupid
        
        data = request.get_json(silent=True)
        if data is None: return 400
        try:
            data = request.get_json()
            player = get_jwt_identity()
            pid = player['id'] 

            update_group(pid=pid, group_data=data, gid=gid)

            db.session.commit()
        except Exception as e:
            logging.exception(e)
            return 400
        
        return 204

    @jwt_required()
    def delete(self, id): # delete group by groupid
        try:
            player = get_jwt_identity()
            pid = player['id'] 

            delete_group(pid=pid, gid=id)

            db.session.commit()
        except Exception as e:
            logging.exception(e)
            return 400
        
        return 204