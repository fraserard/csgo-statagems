
from ..helpers.steam_helper import get_steam_player_data, proper_steam_id_format
from ..helpers.player_helper import add_player_steam, update_player_steam
from ..models.player import Player

def login_create_update_player(sid):
    """Creates or updates Players on login
    
    :param sid: SteamId64 of player
    :return: player_data json if succcess, else raise Exception."""
    if not proper_steam_id_format(sid): 
        raise Exception(f'SteamId not in proper format. Was: {sid}.')
    steam_data = get_steam_player_data(sid)

    player = Player.query.filter_by(steam_id=sid).first()

    # if new registration, make new player from steam api data
    if player is None: player_data = add_player_steam(steam_data) 
    # if player exists, update from steam api data
    else: player_data = update_player_steam(player, steam_data)

    return player_data
