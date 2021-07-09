from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .player import Player
from .match import Match
from .match_player import MatchPlayer
from .map import Map
