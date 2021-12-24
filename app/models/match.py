from datetime import datetime
from app import db 

class Match(db.Model): # single completed match
 
    id: int = db.Column(db.Integer, primary_key=True)
    map_id: int = db.Column(db.Integer, db.ForeignKey('map.id'), nullable=False) # map id
    
    group_id: int = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    date_played: datetime = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
    
    map = db.relationship('Map', back_populates='matches')
    group = db.relationship('Group', back_populates='matches') # a match can be part of one group
    teams = db.relationship('MatchTeam', back_populates='match') # match has 2 teams
    
    # players = db.relationship('MatchPlayer', back_populates='match')
    
    def __repr__(self):
        return f'{self.__class__.__name__}<id: {self.id}>'
