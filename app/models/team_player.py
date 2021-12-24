from datetime import datetime

from app import db

class TeamPlayer(db.Model): # historical view of team, ONLY EVER 5 PLAYERS ON A TEAM
    # only created/updated on Match insert/update
 
    team_id: int = db.Column(db.Integer, db.ForeignKey('team.id'), primary_key=True, autoincrement=False) # team.id, pk
    player_id: int = db.Column(db.Integer, db.ForeignKey('group_player.player_id'), primary_key=True, autoincrement=False) # player.id, pk
    
    kills: int = db.Column(db.SmallInteger, default=0, nullable=False) # total player kills
    assists: int = db.Column(db.SmallInteger, default=0, nullable=False) # total player assists
    deaths: int = db.Column(db.SmallInteger, default=0, nullable=False) # total player deaths
    adr: int = db.Column(db.SmallInteger, default=0, nullable=False) # total player average damage per round
    
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    team = db.relationship('Team', back_populates='members') # a team player is part of a team
    player = db.relationship('GroupPlayer', back_populates='teams') # a group player is part of many group teams
    matches = db.relationship('MatchPlayer', back_populates='team_player')
    
    # __table_args__ = (
    #     db.ForeignKeyConstraint(
    #         ['team_id', 'player_id'],
    #         ['team.id', 'group_player.player_id'],
    #     ),
    # )
    
    def __repr__(self):
        return f'{self.__class__.__name__}<Id: {self.id}, name: {self.group_name}>'

    