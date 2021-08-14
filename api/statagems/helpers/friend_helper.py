from ..extensions import db
from ..models.friend import Friend
from ..models.friend_request import FriendRequest

def get_friends(player): 
    """Gets list of users Player is friends with.

    :param player: Player obj
    :return: List of Player"""
    friends_issued = Friend.player_recipient.query.filter(Friend.player_issuer == player)  
    friends_received = Friend.player_issuer.query.filter(Friend.player_recipient == player)
    friends = friends_issued.union(friends_received).all()
    return friends

def add_friend():
    NotImplemented

def remove_friend():
    NotImplemented

def get_incoming_requests(player): # 
    """Gets list of users who sent friend requests to Player

    :param player: Player obj
    :return: List of Player"""
    incoming_requests = FriendRequest.issuing_user.query(FriendRequest.receiving_user == player)
    return incoming_requests

def get_outgoing_requests(player):
    """Gets list of users who Player sent friend requests to 

    :param player: Player obj
    :return: List of Player"""
    outgoing_requests = FriendRequest.receiving_user.query(FriendRequest.issuing_user == player)
    return outgoing_requests

def send_request():
    NotImplemented
    
def accept_request():
    NotImplemented
