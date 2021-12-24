from datetime import datetime

from app import db

class Team(db.Model): # historical view of team, ONLY EVER 5 PLAYERS ON A TEAM
    # only created/updated on Match insert/update
 
    id: int = db.Column(db.Integer, primary_key=True) # team id
    
    group_id: int = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False) # group id team is part of
    
    games_won: int = db.Column(db.Integer, default=0, nullable=False) # total games won
    games_lost: int = db.Column(db.Integer, default=0, nullable=False) # total games lost
    games_tied: int = db.Column(db.Integer, default=0, nullable=False) # total games tied
    
    rounds_won: int = db.Column(db.Integer, default=0, nullable=False) # total rounds won
    rounds_lost: int = db.Column(db.Integer, default=0, nullable=False) # total rounds lost
    
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    group = db.relationship('Group', back_populates='teams') # a team is part of a group
    matches = db.relationship('MatchTeam', back_populates='team') # a group can have many matches
    members = db.relationship('TeamPlayer', back_populates='team') # a group can have many members

    def __repr__(self):
        return f'{self.__class__.__name__}<Id: {self.id}, name: {self.group_name}>'

    