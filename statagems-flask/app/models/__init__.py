from datetime import datetime

from app import db


# fmt: off
# MIXINS
class GroupAggregates(object):
    games_won: int = db.Column(db.Integer, default=0, nullable=False) # total games won
    games_lost: int = db.Column(db.Integer, default=0, nullable=False) # total games lost
    games_tied: int = db.Column(db.Integer, default=0, nullable=False) # total games tied
    
    rounds_won: int = db.Column(db.Integer, default=0, nullable=False) # total rounds won
    rounds_lost: int = db.Column(db.Integer, default=0, nullable=False) # total rounds lost
    
    times_started_ct: int = db.Column(db.Integer, default=0, nullable=False)
    times_started_t: int = db.Column(db.Integer, default=0, nullable=False)

class IndividualAggregates(object):
    kills: int = db.Column(db.Integer, default=0, nullable=False) # total player kills
    assists: int = db.Column(db.Integer, default=0, nullable=False) # total player assists
    deaths: int = db.Column(db.Integer, default=0, nullable=False) # total player deaths
    adr: int = db.Column(db.SmallInteger, nullable=True) # player average damage per round
    score: int = db.Column(db.Integer, default=0, nullable=False) # total player match score
    mvps: int = db.Column(db.Integer, default=0, nullable=False) # total player mvps
    
    adr_count: int = db.Column(db.Integer, default=0, nullable=False) # times an adr stat has been added, for determining averages
    times_captain: int = db.Column(db.Integer, default=0, nullable=True)
    times_captain_possible: int = db.Column(db.Integer, default=0, nullable=True)
    

class Timestamps(object):
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
from app.models.map import Map
from app.models.match import Match
from app.models.match_player import MatchPlayer
from app.models.match_team import MatchTeam, TeamSides
from app.models.player import Player, PlayerRoles
from app.models.team import Team
from app.models.team_player import TeamPlayer
