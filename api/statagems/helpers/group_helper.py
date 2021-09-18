import logging

from ..models import Group, GroupPlayer, Player
from ..extensions import db

def get_groups_for_player(pid):
    groups = db.session.query(Group).join(Group._members).filter(GroupPlayer.player_id == pid)
    return groups

def create_group(creator_id: int, group_data: dict):
    """Creates new group under Player's id
    
    :param creator_id: id of Player who is creating group
    :param group_data: dict of group data"""
   
    new_group = Group(
        group_name = group_data['group_name'],
        description = None if 'description' not in group_data else group_data['description'],
        creator_id = creator_id,
    )
    db.session.add(new_group)
    db.session.flush()
    
    # auto create groupplayer on group create
    group_member = GroupPlayer(
        player_id = creator_id,
        group_id = new_group.id,
        group_clearance = 0,     
    )
    
    db.session.add(group_member)
        
def update_group(pid: int, group_data: dict, gid: int):
    """Updates group if user has permissions

    :param pid: id of Player who is updating Group
    :param group_data: dict of Group data
    :param gid: id of Group to update"""

    g = Group.query.get(gid)
    if g is None: raise Exception('Group does not exist')
    gp = GroupPlayer.query.filter(GroupPlayer.player_id == pid and GroupPlayer.group_id == gid)
    if gp.group_clearance not in [0,1,2]: raise Exception('Player does not have permissions to update the group')
    
    if 'group_name' in group_data:
        g.group_name = group_data['group_name']
    if 'description' in group_data:
        g.description = group_data['description']

def delete_group(pid: int, gid: int):
    g = Group.query.get(gid)
    if g is None: raise Exception('Group does not exist')
    if g.creator_id != pid: raise Exception('Player does not have permissions to delete the group.')

    db.session.delete(g)

def add_group_member(uid: int, gid: int, pid: int):
    """Adds a group member if user has permissions

    :param uid: id of Player making request
    :param gid: id of Group to modify
    :param pid: id of Player to add to Group"""

    gp = GroupPlayer.query.filter(GroupPlayer.player_id == uid and GroupPlayer.group_id == gid).first() # player making request

    if gp.group_clearance not in [0,1,2]: raise Exception('Player does not have permissions to add group members')

    # CHECK IF PLAYER ALREADY IN GROUP

    group_member = GroupPlayer(
        player_id = pid,
        group_id = gid,     
    )
    
    db.session.add(group_member)

def remove_group_member(uid: int, gid: int, pid: int):
    """Removes a group member if user has permissions

    :param uid: id of Player making request
    :param gid: id of Group to modify
    :param pid: id of Player to remove from Group"""

    # CHECK IF PLAYER IN GROUP

    gps = GroupPlayer.query.filter( (GroupPlayer.player_id == pid or GroupPlayer.player_id == pid) and GroupPlayer.group_id == gid).all()
    logging.error(gps)
    gp = GroupPlayer.query.get(uid, gid) # player making request
    if gp.group_clearance not in [0,1]: raise Exception('Player does not have permissions to remove group members')
    gp_rm = GroupPlayer.query.get(pid, gid) # group member to remove
    if gp.group_clearance >= gp_rm: raise Exception('Player group authority lower than player to remove')

    db.session.delete(gp_rm)

def update_group_member(uid: int, gid: int, pid: int):
    """Updates a group member's permissions if user has permissions

    :param uid: id of Player making request
    :param gid: id of Group to modify
    :param pid: id of Player to update from Group"""

    

    

    

