from datetime import datetime

from app import db

class GroupPlayer(db.Model): # player of group
    
    group_id: int = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True, autoincrement=False) # group id, pk
    player_id: int = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True, autoincrement=False) # player id, pk
    
    group_username: str = db.Column(db.String(64), unique=True, nullable=True) # unique group username

    group_clearance = db.Column(db.Integer, default=16, nullable=False) # player permissions in group
    
    kills: int = db.Column(db.SmallInteger, default=0, nullable=False) # total player kills
    assists: int = db.Column(db.SmallInteger, default=0, nullable=False) # total player assists
    deaths: int = db.Column(db.SmallInteger, default=0, nullable=False) # total player deaths
    adr: int = db.Column(db.SmallInteger, default=0, nullable=False) # player average damage per round
    
    player = db.relationship('Player', back_populates='groups') # a GroupPlayer is a Player
    group = db.relationship('Group', back_populates='members') # a GroupPlayer is part of a Group
    
    teams = db.relationship('TeamPlayer', back_populates='player') # a GroupPlayer is part of many teams
    match_players = db.relationship('MatchPlayer', back_populates='group_player') # a GroupPlayer is part of many matches
    
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f'{self.__class__.__name__}<steamId: {self.group_username}>'

# class Permission:
#     CREATOR = 0
#     REINSTATE_MATCH = 1
#     MODIFY_PLAYER = 2
#     KICK_PLAYER = 3
#     ADD_PLAYER = 4
#     DELETE_MATCH = 5
#     EDIT_MATCH = 6
#     ADD_MATCH = 7
#     VIEW = 16

# roles = {
#             'Creator': [Permission.CREATOR, Permission.REINSTATE_MATCH],
#             'Moderator': [Permission.VIEW, Permission.ADD_MATCH,
#                         Permission.EDIT_MATCH, Permission.DELETE_MATCH,
#                         Permission.ADD_PLAYER, Permission.KICK_PLAYER, Permission.MODIFY_PLAYER],
#             'Referee': [Permission.VIEW, Permission.ADD_MATCH,
#                         Permission.EDIT_MATCH],
#             'Member': [Permission.VIEW]
#         }