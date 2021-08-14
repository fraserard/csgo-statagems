from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from ..extensions import db
from .group_player import GroupPlayer
from .block_list import BlockList
from .friend_request import FriendRequest
from .friend import Friend
from .match_player import MatchPlayer
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import case

class Player(db.Model): # player profile
    __tablename__ = 'player'
 
    id = db.Column(db.Integer, primary_key=True)
    steam_id = db.Column(db.BigInteger, unique=True, nullable=False) # get from steam openid - should be steamId64 format, pk
    username = db.Column(db.String(32), nullable=False) # current in game steam name (ex. faffyy, balbaCREATURE), get from steam (username)
    preferred_username = db.Column(db.String(32), nullable=True) # most common in game name (ex. faffers, balba), manual
    name = db.Column(db.String(32), nullable=True) # first name or otherwise, get from steam (real name), can be null on steam
    avatar_hash = db.Column(db.String(64), nullable=False) # hash of steam profile pic, can get many pic sizes    
    bio = db.Column(db.String(256), nullable=True) # player bio

    last_seen = db.Column(db.DateTime, server_default=db.func.now())
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # matches
    _matches = db.relationship('MatchPlayer', back_populates='player') # a Player is part of many Matches
    matches = association_proxy('_matches', 'match', creator=lambda _p: MatchPlayer(player=_p))

    # friend requests
    issued_requests = db.relationship('FriendRequest', foreign_keys="friend_request.c.issuer_id", back_populates='issuing_user')
    received_requests = db.relationship('FriendRequest', foreign_keys="friend_request.c.recipient_id", back_populates='receiving_user')

    desired_friends = association_proxy('issued_requests', 'receiving_user', creator=lambda _p: FriendRequest(issuing_user=_p)) # users i want to be friends with
    aspiring_friends = association_proxy('received_requests', 'issuing_user') # users who want to be my friend

    # friends
    issued_friends = db.relationship('Friend', foreign_keys="friend.c.player1_id", back_populates='player_issuer') 
    received_friends = db.relationship('Friend', foreign_keys="friend.c.player2_id", back_populates='player_recipient')

    friends_issuer = association_proxy('issued_friends', 'player_issuer', creator=lambda _p: Friend(player_issuer=_p)) # friends where i was the issuer
    friends_recipient = association_proxy('received_friends', 'player_recipient', creator=lambda _p: Friend(player_recipient=_p)) # friends where i was the recipient
    
    # _friends = db.relationship('Player', secondary='friend',
    #         primaryjoin="player.c.id == friend.c.player1_id",
    #         secondaryjoin="player.c.id == friend.c.player2_id",    
    # ) # this method would be better for blocked users

    # blocked users
    issued_blocks = db.relationship('BlockList', foreign_keys="block_list.c.player_id", back_populates='player')
    received_blocks = db.relationship('BlockList', foreign_keys="block_list.c.blocked_player_id", back_populates='blocked_player')

    blocked_players = association_proxy('issued_blocks', 'blocked_player', creator=lambda _p: BlockList(blocked_player=_p)) # players that i have blocked
    players_blocked_by = association_proxy('received_blocks', 'player.id') # players that have blocked me

    # groups
    created_groups = db.relationship('Group', back_populates='creator')
    _groups = db.relationship('GroupPlayer', back_populates='player')
    groups = association_proxy('_groups', 'group', creator=lambda _g: GroupPlayer(group=_g))

    # admin
    acct_type = db.Column(db.String(16), server_default='player', nullable=False) # acccount type: player, admin, etc
    __mapper_args__ = {
        'polymorphic_on':case(
            (acct_type.in_(['player', 'admin']), acct_type), else_='player'),
        'polymorphic_identity':'player',
    }
    def __repr__(self):
        return f'{self.__class__.__name__}<steamId: {self.steam_id}>'
