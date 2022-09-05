
from app import db


# fmt: off
class MatchPlayer(db.Model):  # type: ignore
    """a single player's match stats"""
    match_id: int = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True, autoincrement=False) # match.id, pk
    player_id: int = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True, autoincrement=False) # !!

    team_id: int = db.Column(db.Integer, db.ForeignKey('team.id'), unique=False, index=True, nullable=False) # team.id, PK

    steam_username: str = db.Column(db.String(32), nullable=True) # point-in-time steam in game name
    steam_avatar_hash: str = db.Column(db.String(64), nullable=True) # point-in-time hash of steam profile pic    

    kills: int = db.Column(db.SmallInteger, nullable=False) # total player match kills
    deaths: int = db.Column(db.SmallInteger, nullable=False) # total player match deaths
    assists: int = db.Column(db.SmallInteger, nullable=False) # total player match assists
    adr: int = db.Column(db.SmallInteger, nullable=True) # player match average damage per round
    score: int = db.Column(db.SmallInteger, nullable=True) # total player match score
    mvps: int = db.Column(db.SmallInteger, nullable=True) # total player match mvps

    match_team = db.relationship('MatchTeam', back_populates='players') # match_team has 5 match_player
    player = db.relationship('Player', back_populates='matches') # Player profile

    # team_player = db.relationship('TeamPlayer', back_populates='matches')
    # match = db.relationship('Match', back_populates='players') # a Match consists of many MatchPlayers    

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['match_id', 'team_id'],
            ['match_team.match_id', 'match_team.team_id'],
        ),
        # db.ForeignKeyConstraint(
        #     ['player_id', 'team_id'],
        #     ['team_player.player_id', 'team_player.team_id'],
        # ),
    )

    def __repr__(self):
        return f'{self.__class__.__name__}<match_id: {self.match_id}, team_id: {self.team_id}, player_id: {self.player_id}>'
