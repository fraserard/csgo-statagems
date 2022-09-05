from enum import Enum

from app import db


# fmt: off
class TeamSides(Enum):
    CT = 'CT'
    T = 'T'
 
class MatchTeam(db.Model): # type: ignore  
    """single team of completed match"""
    
    match_id: int = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True, autoincrement=False) # match id, pk 
    team_id: int = db.Column(db.Integer, db.ForeignKey('team.id'), primary_key=True, autoincrement=False) # team id, pk
    
    # team_hash: str = db.Column(db.String(55), unique=False, autoincrement=False) # hash of ascending player.ids, "2_8_20_34_40"
    
    start_side: TeamSides = db.Column(db.Enum(TeamSides), nullable=False) # must be either 'CT' or 'T'
    captain_id: int = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=True) # group_player_id of team captain
    
    rounds_won: int = db.Column(db.SmallInteger, nullable=False) # total rounds won
    
    players = db.relationship('MatchPlayer', back_populates='match_team', order_by='desc(MatchPlayer.kills)') # match_team has 5 match_player
    match = db.relationship('Match', back_populates='teams') # match_team is part of 1 match
    team = db.relationship('Team', back_populates='matches') # a MatchTeam has one Team
             
    def __repr__(self):
        return f'{self.__class__.__name__}<match_id: {self.match_id}>'
