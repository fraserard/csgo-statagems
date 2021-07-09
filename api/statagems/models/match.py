from . import db

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
        return f'{self.__class__.__name__}<matchId: {self.match_id}, datePlayed: {self.date_played}, score: {self.team1_score}-{self.team2_score}>'