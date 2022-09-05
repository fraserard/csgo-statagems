from typing import TYPE_CHECKING

from app import db
from app.models import IndividualAggregates

if TYPE_CHECKING:
    from app.models import Player, Team

# fmt: off
class TeamPlayer(IndividualAggregates, db.Model): # type: ignore
    """Historical view of team, ONLY EVER 5 PLAYERS ON A TEAM.
    Created/Modified on Match insert/update"""
    
    team_id: int = db.Column(db.Integer, db.ForeignKey('team.id'), primary_key=True, autoincrement=False) 
    # team.id, PK
    player_id: int = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True, autoincrement=False) # player's id, PK
    
    team: 'Team' = db.relationship('Team', back_populates='members') # a team player is part of a team
    player: 'Player' = db.relationship('Player', back_populates='teams') # a group player is part of many group teams
    
    # IndividualAggregates
    
    def __repr__(self):
        return f'{self.__class__.__name__}<Id: {self.id}, name: {self.group_name}>'
