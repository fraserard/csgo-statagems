from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

class Player(db.Model): # player profile
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    steamId = db.Column(db.Integer, unique=True, nullable=True)
    username = db.Column(db.String(32), nullable=False)
    firstName = db.Column(db.String(32), nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    matches = db.relationship('MatchPlayer', back_populates='player')

    def __repr__(self):
        return '<Id: %r, Username: %r>' % self.id, self.username

    
class Match(db.Model): # end of match stats
    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True)
    # gameType = db.Column(db.String(2), nullable=False) # either 'mm' (matchmaking) or '10' (10 man), leave out - just do 10 man stats
    datePlayed = db.Column(db.DateTime, nullable=True)
    team1Score = db.Column(db.Integer, nullable=False)
    team2Score = db.Column(db.Integer, nullable=False)
    team1StartingSide = db.Column(db.String(2), nullable=False) # either 'CT' or 'T'
    #mapId - make map table, pk - map file name, map full name
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    players = db.relationship('MatchPlayer', back_populates='match')
    #rounds - make round table, round_player table. store data from every round.

class MatchPlayer(db.Model): # end of game stats for each player
    __tablename__ = 'match_player'

    playerId = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True, autoincrement=False)
    matchId = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True, autoincrement=False)
    isTeam1 = db.Column(db.Boolean, nullable=False) # true = team1, false = team2
    isCaptain = db.Column(db.Boolean, nullable=True) # is player team captain?, nullable cuz info might be unavailable
    kills = db.Column(db.SmallInteger, nullable=False)
    assists = db.Column(db.SmallInteger, nullable=False)
    deaths = db.Column(db.SmallInteger, nullable=False)
    #adr = db.Column(db.SmallInteger, nullable=False) make part of round table ^^^

    match = db.relationship('Match', back_populates='players')
    player = db.relationship('Player', back_populates='matches')





