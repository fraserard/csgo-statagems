from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

class Gamer(db.Model): #TEST - remove whenever
    __tablename__ = 'gamer'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    rank = db.Column(db.String(50))

    def __repr__(self):
        return '<Id: %r, Username: %r, Rank: %r>' % self.id, self.username, self.rank
        #return f"{self.username} ({self.rank})"

players_teams = db.Table('players_teams',  #many to many, players can be on many teams, teams have many players
            db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True),
            db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True)
            )

class Player(db.Model): # player profile
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    steamId = db.Column(db.Integer, unique=True, nullable=True)
    username = db.Column(db.String(32), nullable=False)
    firstName = db.Column(db.String(32), nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    teams = db.relationship('Team', secondary=players_teams)
    matches = db.relationship('MatchPlayer', back_populates='player')

    def __repr__(self):
        return '<Id: %r, Username: %r, Rank: %r>' % self.id, self.username, self.rank

class Team(db.Model): # one team of 5 players
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    wins = db.Column(db.Integer, server_default=0)
    losses = db.Column(db.Integer, server_default=0)

    created_at = db.Column(db.DateTime, server_default=db.func.now())

    players = db.relationship('Player', secondary=players_teams)
    matchTeams = db.relationship('MatchTeam', back_populates='team')

class Match(db.Model): # end of match stats
    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True)
    gameType = db.Column(db.String(2), nullable=False) # either 'mm' (matchmaking) or '10' (10 man)
    #team1Id = db.Column(db.Integer, nullable=False)
    #team2Id = db.Column(db.Integer, nullable=False) 
    winnerRoundsWon = db.Column(db.Integer, nullable=True)
    loserRoundsWon = db.Column(db.Integer, nullable=True)
    datePlayed = db.Column(db.DateTime, nullable=True)
    #rounds - make round table, round_player table. store data from every round.

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    teams = db.relationship('MatchTeam', back_populates='match')
    
class MatchTeam(db.Model): # end of match stats for each team
    __tablename__ = 'match_team'

    matchId = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True, autoincrement=False)
    teamId = db.Column(db.Integer, db.ForeignKey('team.id'), primary_key=True, autoincrement=False) # if MM game, id of -1, don't save to team table
    result = db.Column(db.String(1), nullable=False) # 'W' won or 'L' lost
    roundsWon = db.Column(db.Integer, nullable=False)

    matchPlayers = db.relationship('MatchPlayer', back_populates='matchTeam', lazy=True)
    match = db.relationship('Match', back_populates='teams')
    team = db.relationship('Team', back_populates='matchTeams')

class MatchPlayer(db.Model): # end of game stats for each player
    __tablename__ = 'match_player'

    playerId = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True, autoincrement=False)
    matchTeamId = db.Column(db.Integer, db.ForeignKey('match_team.id'), primary_key=True, autoincrement=False)
    #matchId = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True, autoincrement=False)
    kills = db.Column(db.SmallInteger, nullable=False)
    assists = db.Column(db.SmallInteger, nullable=False)
    deaths = db.Column(db.SmallInteger, nullable=False)
    adr = db.Column(db.SmallInteger, nullable=False)

    player = db.relationship('Player', back_populates='matches')
    matchTeam = db.relationship("MatchTeam", back_populates='matchPlayers', lazy=True)





