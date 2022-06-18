from datetime import datetime
from typing import TYPE_CHECKING

from app import db

if TYPE_CHECKING:
    from app.models.map import Map
    from app.models.match_team import MatchTeam

# fmt: off
class Match(db.Model): # type: ignore 
    """single completed match"""
    
    id: int = db.Column(db.Integer, primary_key=True)
    map_id: int = db.Column(db.Integer, db.ForeignKey('map.id'), nullable=False) # map id

    date_played: datetime = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
    
    map: 'Map' = db.relationship('Map', back_populates='matches')
    teams: list['MatchTeam'] = db.relationship('MatchTeam', back_populates='match') # match has 2 teams
    
    # players = db.relationship('MatchPlayer', back_populates='match') # a Match consists of many MatchPlayers

    def __repr__(self):
        return f'{self.__class__.__name__}<id: {self.id}>'
