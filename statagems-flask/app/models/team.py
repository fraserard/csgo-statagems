from typing import TYPE_CHECKING

from app import db
from app.models import GroupAggregates, Timestamps

if TYPE_CHECKING:
    from app.models import MatchTeam, TeamPlayer

# fmt: off
class Team(GroupAggregates, Timestamps, db.Model): # type: ignore
    """Historical view of team, ONLY EVER 5 PLAYERS ON A TEAM.
    Created/Modified on Match insert/update"""
 
    id: int = db.Column(db.Integer, primary_key=True) # team id
    team_hash: str = db.Column(db.String(55), index=True, unique=True, nullable=False) # hash of group_player.ids 
    
    matches: 'MatchTeam' = db.relationship('MatchTeam', back_populates='team') # a team can have many matches
    members: list['TeamPlayer'] = db.relationship('TeamPlayer', back_populates='team') # a team has 5 players
    
    def __repr__(self):
        return f'{self.__class__.__name__}<Id: {self.id}, name: {self.group_name}>'
