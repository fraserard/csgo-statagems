from sqlalchemy.sql.expression import exists
from ..models.player import Player
from ..extensions import db
import logging
from .steam_helper import proper_steam_id_format, get_steam_player_data
from ..schemas.player_schemas import player_schema

def add_player_steam(steam_data):
    """Adds new player to db based on data retrieved from Steam API. 
    
    :param steam_data: New data to create player with
    :return: player_data json if succcess, else raise Exception."""

    try:
        new_player = Player(
            steam_id = steam_data['steamid'],
            username = steam_data['personaname'],
            avatar_hash = steam_data['avatarhash'] )
        if 'realname' in steam_data:
            new_player.name = (steam_data['realname'])[:32]
        
        db.session.add(new_player)
     
        return player_schema.dump(Player.query.filter_by(steam_id=new_player.steam_id).first())
    except Exception as e: raise e

def update_player_steam(player, steam_data):
    """Updates player based on data retrieved from Steam API. 
    
    :param player: Player to update from 'Player.query'
    :param steam_data: New data to update player with
    :return: player_data json if succcess, else raise Exception."""

    try:
        if player.username != steam_data['personaname']:
            player.username = steam_data['personaname']

        if 'realname' in steam_data:
            if player.name != steam_data['realname']:
                player.name = (steam_data['realname'])[:32] # String max length = 32

        if player.avatar_hash != steam_data['avatarhash']:
            player.avatar_hash = steam_data['avatarhash']
    
        return player_schema.dump(player)
    except Exception as e: raise e

def new_player_by_steam_id(sid): # alter to allow list of steamIds
    """Creates new player using data from Steam API using param SteamId
    
    :param sid: SteamId64 of Player to create
    :return: player_data json if succcess, else raise Exception."""

    if not proper_steam_id_format(sid): 
        raise Exception(f'SteamId not in proper format, was: {sid}')
    if Player.query.filter_by(steam_id=sid).first():
        raise Exception(f'Player with SteamId: {sid}, already exists')
    player_data = get_steam_player_data(sid)
    player_data = add_player_steam(player_data)

    return player_data
        
    
    
     