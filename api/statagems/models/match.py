from ..extensions import db
from .match_player import MatchPlayer
from sqlalchemy.ext.associationproxy import association_proxy

class Match(db.Model): # end of match stats
    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True) # match id, pk
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=True) # group id match belongs too, if None: match is an mm game
    date_played = db.Column(db.DateTime, nullable=True) # date match played
    team1_score = db.Column(db.Integer, nullable=False) # team 1 score ex. 16, 14, if match not played set to 0
    team2_score = db.Column(db.Integer, nullable=False) # team 2 score ex. 8, 16, if match not played set to 0
    team1_start_side = db.Column(db.String(2), nullable=False) # team 1 starting side - either 'CT' or 'T'
    map_id = db.Column(db.Integer, db.ForeignKey('map.id'), nullable=False) # map id
    # match_notes - add optional match notes

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    _players = db.relationship('MatchPlayer', back_populates='match') # a Match consists of many MatchPlayers
    players = association_proxy('_players', 'player', creator=lambda _p: MatchPlayer(player=_p))

    map = db.relationship('Map', back_populates='matches') # a single Map is played in many Matches
    map_name = association_proxy('map', 'map_name')
    group = db.relationship('Group', back_populates='matches') # a match belongs to a single group
    #rounds - make round table, round_player table. store data from every round.

    def __repr__(self):
        return f'{self.__class__.__name__}<matchId: {self.match_id}, datePlayed: {self.date_played}, score: {self.team1_score}-{self.team2_score}>'