from ..extensions import db
from .group_player import GroupPlayer
from sqlalchemy.ext.associationproxy import association_proxy

class Group(db.Model): # groups, users can join
    __tablename__ = 'group'
 
    id = db.Column(db.Integer, primary_key=True) # group id
    group_name = db.Column(db.String(32), nullable=False) # name of group
    description = db.Column(db.String(255), nullable=True) # description of group
    creator_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False) # user id of group creator

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), server_onupdate=db.FetchedValue())

    creator = db.relationship('Player', back_populates='created_groups') # a group has one creator
    matches = db.relationship('Match', back_populates='group') # a group can have many matches

    _members = db.relationship('GroupPlayer', back_populates='group') # a group can have many members
    members = association_proxy('_members', 'player', creator=lambda _p: GroupPlayer(player=_p))


    
    def __repr__(self):
        return f'{self.__class__.__name__}<steamId: {self.group_name}>'