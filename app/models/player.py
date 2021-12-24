from datetime import datetime

from flask import current_app
from app import db 
    
class Player(db.Model): # player profile
 
    id: int = db.Column(db.Integer, primary_key=True)
    steam_id: int = db.Column(db.BigInteger, unique=True, nullable=False) # steamid64
    steam_username: str = db.Column(db.String(32), nullable=False) # current steam in game name
    steam_real_name: str = db.Column(db.String(64), nullable=True) # steam real name, can be null on steam
    steam_avatar_hash: str = db.Column(db.String(64), nullable=False) # hash of steam profile pic    
    is_admin: bool = db.Column(db.Boolean(), default=False, nullable=False)
        
    last_fetched_steam: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_seen: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    groups = db.relationship('GroupPlayer', back_populates='player') # a Player can be in many Groups
    
    # # matches
    # matches = db.relationship('MatchPlayer', back_populates='player') # a Player is part of many Matches
    
    def can_fetch_steam(self):
        if self.last_fetched_steam < datetime.utcnow() - current_app.config['STEAM_API_COOLDOWN']:
            return True
        return False
    
    # @staticmethod        
    # def get_by_steam_id(steam_id: int) -> 'Player':
    #     return Player.query.\
    #             add_columns(Player.id, Player.steam_id,
    #                         Player.steam_username, Player.steam_real_name, 
    #                         Player.steam_avatar_hash, Player.last_fetched_steam,
    #                         Player.is_admin, Player.last_seen).\
    #             filter_by(steam_id = steam_id).first()
    #     return Player.query.filter_by(steam_id = steam_id).first()

    def __repr__(self):
        return f'{self.__class__.__name__}<id: {self.id}, steam_id: {self.steam_id}, steam_username:{self.steam_username}>'
