
from app import db 

class MatchTeam(db.Model): # single team of completed match
 
    match_id: int = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True, autoincrement=False) # match id, pk
    team_id: int = db.Column(db.Integer, db.ForeignKey('team.id'), primary_key=True, autoincrement=False)
    
    start_side: str = db.Column(db.String(2), nullable=False) # 'CT', 'T'
    
    captain_id: int = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=True) # player id of team captain
    
    rounds_won: int = db.Column(db.SmallInteger, nullable=False) # total rounds won
    
    players = db.relationship('MatchPlayer', back_populates='match_team') # match_team has 5 match_player
    match = db.relationship('Match', back_populates='teams') # match_team is part of 1 match
    team = db.relationship('Team', back_populates='matches')
    
    
    # __table_args__ = (
    #     db.ForeignKeyConstraint(
    #         ['match_id', 'team_id'],
    #         ['match.id', 'team.id'],
    #     ),
    # )
                  
    def __repr__(self):
        return f'{self.__class__.__name__}<id: {self.id}>'
