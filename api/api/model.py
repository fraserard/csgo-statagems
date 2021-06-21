from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

class Player(db.Model): # player profile
    __tablename__ = 'player'
 
    steamId = db.Column(db.Integer, primary_key=True) # get from steam openid - should be steamId64 format, pk
    username = db.Column(db.String(32), nullable=False) # current in game steam name (ex. faffyy, balbaCREATURE), get from steam
    preferredUsername = db.Column(db.String(32), nullable=False) # most common in game name (ex. faffers, balba), manual
    name = db.Column(db.String(32), nullable=False) # first name or otherwise

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    matches = db.relationship('MatchPlayer', back_populates='player') # a Player is part of many matches

    def __repr__(self):
        return '<steamId: %r, preferredUsername: %r>' % self.steamId, self.preferredUsername

    
class Match(db.Model): # end of match stats
    __tablename__ = 'match'

    matchId = db.Column(db.Integer, primary_key=True) # match id, pk
    #gameType = db.Column(db.String(2), nullable=False) # either 'mm' (matchmaking) or '10' (10 man), leave out - just do 10 man stats
    datePlayed = db.Column(db.DateTime, nullable=True) # date match played
    team1Score = db.Column(db.Integer, nullable=False) # team 1 score ex. 16, 14, if match not played set to 0
    team2Score = db.Column(db.Integer, nullable=False) # team 2 score ex. 8, 16, if match not played set to 0
    team1StartingSide = db.Column(db.String(2), nullable=False) # team 1 starting side - either 'CT' or 'T'
    mapFilename = db.Column(db.Column(db.String(32), db.ForeignKey('map.filename'), nullable=False)) # map filename
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    players = db.relationship('MatchPlayer', back_populates='match') # a Match consists of many MatchPlayers
    map = db.relationship('Map', back_populates='matches') # a single Map is played in many Matches
    #rounds - make round table, round_player table. store data from every round.

    def __repr__(self):
        return '<matchId: %r, datePlayed: %r, score: %r-%r, map: %r>' % self.matchId, self.datePlayed, self.team1Score, self.team2Score, self.mapFilename

class MatchPlayer(db.Model): # end of game stats for each player
    __tablename__ = 'match_player'

    playerId = db.Column(db.Integer, db.ForeignKey('player.steamId'), primary_key=True, autoincrement=False) # player id, pk
    matchId = db.Column(db.Integer, db.ForeignKey('match.matchId'), primary_key=True, autoincrement=False) # match id, pk
    isTeam1 = db.Column(db.Boolean, nullable=False) # true = team1, false = team2
    isCaptain = db.Column(db.Boolean, server_default=db.true(), nullable=False) # is player team captain? if unknown = false
    kills = db.Column(db.SmallInteger, nullable=False) # total kills
    assists = db.Column(db.SmallInteger, nullable=False) # total assists
    deaths = db.Column(db.SmallInteger, nullable=False) # total deaths
    adr = db.Column(db.Float, nullable=True) # average damage per round - make part of round table (adr, kills, assists, deaths)

    match = db.relationship('Match', back_populates='players') # a Match consists of many MatchPlayers
    player = db.relationship('Player', back_populates='matches') # a Player is part of many Matches

    def __repr__(self):
        return '<playerId: %r, matchId: %r, isTeam1: %r, isCaptain: %r, kills: %r, deaths: %r>' % self.playerId, self.matchId, self.isTeam1, self.isCaptain, self.kills, self.deaths

class Map(db.Model): # map info
    __tablename__ = 'map'

    filename = db.Column(db.String(32), primary_key=True) # ex. de_dust2, de_cbble, pk
    mapName = db.Column(db.String(32), unique=True) # ex. Dust II, Cobblestone
    # anything else? image column ?

    matches = db.relationship('Match', back_populates='map') # a Map is played in many Matches

    def __repr__(self):
        return '<filename: %r, mapName: %r>' % self.filename, self.mapName





