from app import db

# fmt: off
class Invitable(db.Model):   # type: ignore
    """a player available for invite"""
    
    steam_id: int = db.Column(db.BigInteger, auto_increment=False, primary_key=True) # steamid64
    steam_username: str = db.Column(db.String(32), nullable=False) # current steam in game name
    steam_real_name: str = db.Column(db.String(64), nullable=True) # steam real name, can be null on steam
    steam_avatar_hash: str = db.Column(db.String(64), nullable=False) # hash of steam profile pic   


    def __repr__(self):
        return f'{self.__class__.__name__}<steam_id: {self.steam_id}, steam_username:{self.steam_username}>'
