from ..extensions import db

class Player(db.Model): # player profile
    __tablename__ = 'player'
 
    id = db.Column(db.Integer, primary_key=True)
    steam_id = db.Column(db.BigInteger, unique=True, nullable=False) # get from steam openid - should be steamId64 format, pk
    username = db.Column(db.String(32), nullable=False) # current in game steam name (ex. faffyy, balbaCREATURE), get from steam (username)
    preferred_username = db.Column(db.String(32), nullable=True) # most common in game name (ex. faffers, balba), manual
    name = db.Column(db.String(32), nullable=False) # first name or otherwise, get from steam (real name)
    profile_pic_url = db.Column(db.Text, nullable=False) # url of steam profile picture, full size

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    matches = db.relationship('MatchPlayer', back_populates='player') # a Player is part of many Matches

    def __repr__(self):
        return f'{self.__class__.__name__}<steamId: {self.steam_id}>'