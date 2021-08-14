# group_id, player_id, group_clearance
from ..extensions import db

class GroupPlayer(db.Model): # player of group
    __tablename__ = 'group_player'
 
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True, autoincrement=False) # player id, pk
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True, autoincrement=False) # group id, pk
    group_clearance = db.Column(db.Integer, nullable=False) # player permissions in group
    
    player = db.relationship('Player', back_populates='_groups') # a Player is part of many Groups
    group = db.relationship('Group', back_populates='_members') # a Group can have many Members
    
    def __repr__(self):
        return f'{self.__class__.__name__}<steamId: {self.steam_id}>'