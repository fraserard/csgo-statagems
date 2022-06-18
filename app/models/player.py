from datetime import datetime
from typing import TYPE_CHECKING
from enum import Enum

from app import db
from app.models import IndividualAggregates, GroupAggregates, Timestamps
from app.steam_api import SteamAPI

if TYPE_CHECKING:
    from app.models import MatchPlayer, TeamPlayer


# fmt: off
class PlayerRoles(Enum):
    ADMIN = "ADMIN"  # only one admin
    MOD = "MOD"  # can manage players
    REF = "REF"  # can manage matches
    USER = "USER"  # is whitelisted


class Player(IndividualAggregates, GroupAggregates, Timestamps, db.Model): # type: ignore 
    """Player profile"""
    id: int = db.Column(db.Integer, primary_key=True)
    steam_id: str = db.Column(db.BigInteger, unique=True, nullable=False) # steamid64
    steam_username: str = db.Column(db.String(32), nullable=False) # current steam in game name
    steam_real_name: str | None = db.Column(db.String(64), nullable=True) # steam real name, can be null on steam
    steam_avatar_hash: str = db.Column(db.String(64), nullable=False) # hash of steam profile pic   
    last_fetched_steam: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False) # last SteamAPI usage
    
    role: PlayerRoles = db.Column(db.Enum(PlayerRoles), default=PlayerRoles.USER, nullable=False)   
    
    last_seen: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False) # last logged on
    
    matches: list['MatchPlayer'] = db.relationship('MatchPlayer', back_populates='player') # a Player can be in many Matches
    
    teams: list['TeamPlayer'] = db.relationship('TeamPlayer', back_populates='player')
    
    def refresh_steam_data(self):
        players = Player._players_from_steam([self.steam_id])
        fresh_player = players[0]
        
        # update fields
        self.steam_username = fresh_player.steam_username
        self.steam_avatar_hash = fresh_player.steam_avatar_hash
        self.steam_real_name = fresh_player.steam_real_name
        self.last_fetched_steam = datetime.utcnow()
    
    @staticmethod
    def _players_from_steam(steam_ids: list[str]) -> 'list[Player]':
        """steam_ids max size 99"""
        
      
        if len(steam_ids) > 99: raise ValueError
            
        steam_api = SteamAPI()
        steam_players_data = steam_api.get_player_summaries(steam_ids)
        
        players = []   
        for player_data in steam_players_data:
            player = Player()
            player.steam_id = player_data['steamid']
            player.steam_username = player_data['personaname']
            player.steam_avatar_hash = player_data['avatarhash']
            player.steam_real_name = player_data['realname'] if 'realname' in player_data else None
            
            players.append(player)
        
        return players
    
    @staticmethod        
    def get_by_steam_id(steam_id: str) -> 'Player':
        return Player.query.filter_by(steam_id = steam_id).first()
    
    @staticmethod
    def whitelist(steam_ids: list[str]):
        """whitelist players by steamid"""
          
        players = Player._players_from_steam(steam_ids)
        db.session.add_all(players)

    def __repr__(self):
        return f'{self.__class__.__name__}<id: {self.id}, steam_id: {self.steam_id}, steam_username:{self.steam_username}>'
