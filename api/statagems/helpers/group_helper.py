import logging
from ..models import Group, GroupPlayer
from ..extensions import db

def get_groups_for_player(pid):
    NotImplemented

def create_group(creator_id: int, group_data: dict):
    """Creates new group under Player's id
    
    :param creator_id: id of Player who is creating group
    :param group_data: dict of group data
    :return: player_data json if succcess, else raise Exception."""

    try:
        new_group = Group(
            group_name = group_data['group_name'],
            description = None if 'description' not in group_data else group_data['description'],
            creator_id = creator_id,
        )
        db.session.add(new_group)
        db.session.flush()
        logging.error(new_group)
        # auto create groupplayer on group create
        group_member = GroupPlayer(
            player_id = creator_id,
            group_id = new_group.id,
            group_clearance = 0,     
        )
        logging.error(group_member)
        db.session.add(group_member)
        db.session.commit()
    except Exception as e: raise e
    

def add_group_member():
    NotImplemented

def remove_group_member():
    NotImplemented