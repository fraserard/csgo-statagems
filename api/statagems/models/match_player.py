from ..extensions import db

class MatchPlayer(db.Model): # end of game stats for each player
    __tablename__ = 'match_player'

    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True, autoincrement=False) # player id, pk
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True, autoincrement=False) # match id, pk
    is_team1 = db.Column(db.Boolean, nullable=False) # true = team1, false = team2
    is_captain = db.Column(db.Boolean, server_default=db.true(), nullable=False) # is player team captain? if unknown = false
    kills = db.Column(db.SmallInteger, nullable=False) # total match kills
    assists = db.Column(db.SmallInteger, nullable=False) # total match assists
    deaths = db.Column(db.SmallInteger, nullable=False) # total match deaths
    adr = db.Column(db.Float, nullable=True) # average damage per round - make part of round table (adr, kills, assists, deaths)

    match = db.relationship('Match', back_populates='_players') # a Match consists of many MatchPlayers
    player = db.relationship('Player', back_populates='_matches') # a Player is part of many Matches

    def __repr__(self):
        return f'{self.__class__.__name__}<playerId: {self.player_id}, matchId: {self.match_id}, isTeam1: {self.is_team1}>'