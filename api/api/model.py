from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model): # player profile
    __tablename__ = 'player'
 
    id = db.Column(db.Integer, primary_key=True)
    steam_id = db.Column(db.BigInteger, nullable=False) # get from steam openid - should be steamId64 format, pk
    username = db.Column(db.String(32), nullable=False) # current in game steam name (ex. faffyy, balbaCREATURE), get from steam
    preferred_username = db.Column(db.String(32), nullable=False) # most common in game name (ex. faffers, balba), manual
    name = db.Column(db.String(32), nullable=False) # first name or otherwise

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    matches = db.relationship('MatchPlayer', back_populates='player') # a Player is part of many Matches

    def __repr__(self):
        return f'{self.__class__.__name__}<steamId: {self.steam_id}>'
        #return '<steamId: %r, username: %r, preferredUsername: %r, name: %r>' % self.steamId, self.username, self.preferredUsername, self.name
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    
class Match(db.Model): # end of match stats
    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True) # match id, pk
    #gameType = db.Column(db.String(2), nullable=False) # either 'mm' (matchmaking) or '10' (10 man), leave out - just do 10 man stats
    date_played = db.Column(db.DateTime, nullable=True) # date match played
    team1_score = db.Column(db.Integer, nullable=False) # team 1 score ex. 16, 14, if match not played set to 0
    team2_score = db.Column(db.Integer, nullable=False) # team 2 score ex. 8, 16, if match not played set to 0
    team1_start_side = db.Column(db.String(2), nullable=False) # team 1 starting side - either 'CT' or 'T'
    map_filename = db.Column(db.String(32), db.ForeignKey('map.filename'), nullable=False) # map filename
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    players = db.relationship('MatchPlayer', back_populates='match') # a Match consists of many MatchPlayers
    map = db.relationship('Map', back_populates='matches') # a single Map is played in many Matches
    #rounds - make round table, round_player table. store data from every round.

    def __repr__(self):
        return '<matchId: %r, datePlayed: %r, score: %r-%r, map: %r>' % self.match_id, self.date_played, self.team1_score, self.team2_score, self.map_filename

class MatchPlayer(db.Model): # end of game stats for each player
    __tablename__ = 'match_player'

    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True, autoincrement=False) # player id, pk
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True, autoincrement=False) # match id, pk
    is_team1 = db.Column(db.Boolean, nullable=False) # true = team1, false = team2
    is_captain = db.Column(db.Boolean, server_default=db.true(), nullable=False) # is player team captain? if unknown = false
    kills = db.Column(db.SmallInteger, nullable=False) # total kills
    assists = db.Column(db.SmallInteger, nullable=False) # total assists
    deaths = db.Column(db.SmallInteger, nullable=False) # total deaths
    adr = db.Column(db.Float, nullable=True) # average damage per round - make part of round table (adr, kills, assists, deaths)

    match = db.relationship('Match', back_populates='players') # a Match consists of many MatchPlayers
    player = db.relationship('Player', back_populates='matches') # a Player is part of many Matches

    def __repr__(self):
        return '<playerId: %r, matchId: %r, isTeam1: %r, isCaptain: %r, kills: %r>' % self.player_id, self.match_id, self.is_team1, self.is_captain, self.kills

class Map(db.Model): # map info
    __tablename__ = 'map'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(32), unique=True) # ex. de_dust2, de_cbble, pk
    map_name = db.Column(db.String(32), unique=True) # ex. Dust II, Cobblestone
    # anything else? image column ?

    matches = db.relationship('Match', back_populates='map') # a Map is played in many Matches

    def __repr__(self):
        return '{self.__class__.__name__}<file: {self.filename}, name: {self.mapName}>'.format(self=self)
        





