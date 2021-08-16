import logging

from ..models import Group, GroupPlayer, Player
from ..extensions import db

def get_groups_for_player(pid):
    NotImplemented

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
    """Updates group with data, if user has permissions

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
    gp = GroupPlayer.query.filter(GroupPlayer.player_id == pid and GroupPlayer.group_id == gid)
    if gp.group_clearance not in [0,1]: raise Exception('Player does not have permissions to update the group')

    db.session.delete(g)

def add_group_member():
    NotImplemented

def remove_group_member():
    NotImplemented