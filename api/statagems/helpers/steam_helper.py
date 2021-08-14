import logging, re, requests
from ..constants import STEAM_API_KEY

def proper_steam_id_format(sid):
    """Checks if input is in correct 64 bit SteamId format.

    :param sid: SteamId64 to validate.
    :return: True if SteamID is valid format, else False."""
    sid = str(sid)
    if re.search("^(7656[0-9]{13})$", sid) is None or sid is None:
        return False
    else: return True

def get_steam_player_data(sid):
    """Retrieve SteamApi GetPlayerSummaries data for input SteamID.

    :param steam_id64: SteamID64 to get data for.
    :return: steam_player_data json if succcess, else raise Exception."""
        
    resp = requests.get(f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={STEAM_API_KEY}&steamids={sid}')
    if resp.status_code == 403: 
        logging.critical('403 error accessing steam api. invalid steam api key.')
        raise Exception('403 error accessing steam api. invalid steam api key.')
    player_data = resp.json()
    player_data = player_data['response']['players'][0]

    if player_data is None: raise Exception(f'Error, no player data found for SteamId: {sid}')
        
    return player_data
