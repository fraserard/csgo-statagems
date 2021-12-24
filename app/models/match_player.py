from app import db
from app.models import match 

class MatchPlayer(db.Model): # match single player stats
 
    match_id: int = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True, autoincrement=False) # match.id, pk
    player_id: int = db.Column(db.Integer, db.ForeignKey('group_player.player_id'), primary_key=True, autoincrement=False) # player.id, pk
    
    team_id: int = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False) # team.id, pk
    
    steam_username: str = db.Column(db.String(32), nullable=False) # point-in-time steam in game name
    steam_avatar_hash: str = db.Column(db.String(64), nullable=False) # point-in-time hash of steam profile pic    
    
    kills: int = db.Column(db.SmallInteger, nullable=False) # total player kills
    assists: int = db.Column(db.SmallInteger, nullable=False) # total player assists
    deaths: int = db.Column(db.SmallInteger, nullable=False) # total player deaths
    adr: int = db.Column(db.SmallInteger, nullable=False) # player average damage per round
    
    match_team = db.relationship('MatchTeam', foreign_keys=[match_id, team_id], back_populates='players') # match_team has 5 match_player
    group_player = db.relationship('GroupPlayer', back_populates='match_players')
    
    # match = db.relationship('Match', back_populates='players') # MatchPlayer is part of 1 match
    
    # team = db.relationship('Team') # match_team is part of 1 team
    team_player = db.relationship('TeamPlayer', back_populates='matches')
    
    __table_args__ = (
        db.ForeignKeyConstraint(
            ['match_id', 'team_id'],
            ['match_team.match_id', 'match_team.team_id'],
        ),
        db.ForeignKeyConstraint(
            ['team_id', 'player_id'],
            ['team_player.team_id', 'team_player.player_id'],
        ),
    )
          
    def __repr__(self):
        return f'{self.__class__.__name__}<match_id: {self.match_id}, team_id: {self.team_id}, player_id: {self.player_id}>'