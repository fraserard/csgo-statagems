# from typing import TYPE_CHECKING, List, Dict
# import re as regex

# from api.exceptions import InputError
# from api.extensions import steam_api
# from api.schemas.player_schemas import player_steam_schema, players_steam_schema

# def is_valid_steam_id(steam_id) -> bool:
#     """Checks if input is in 64 bit SteamId format."""

#     steam_id = str(steam_id)
#     if regex.search("^(7656[0-9]{13})$", steam_id) is None or steam_id is None:
#         return False
#     return True

# def get_players_from_steam(steam_id_list: List[int]) -> Dict[str,Dict[str,str]]:
#     """Call SteamApi GetPlayerSummaries for Steam Ids. raises InputError"""

#     if len(steam_id_list) > 99:
#         InputError('max 100 steam ids at one time')
        
#     steam_id_list_string = ','.join(steam_id_list)
    
#     steam_players_data = steam_api.get_player_summaries(steam_id_list_string)
        
#     steam_players_data = steam_players_data['response']['players']

#     if steam_players_data is None: 
#         raise InputError('no steam player data for steam id')
    
#     return players_steam_schema.load(steam_players_data)

# def get_player_from_steam(steam_id: int) -> Player:
#     """Call SteamAPI GetPlayerSummaries for given Steam ID. Returns dict. Raises InputError"""

#     # https://partner.steamgames.com/doc/webapi/ISteamUser#GetPlayerSummaries       
    
#     steam_player_data = steam_api.get_player_summaries(steam_id)

#     steam_player_data = steam_player_data['response']['players'][0]

#     if steam_player_data is None: 
#         raise InputError('no steam player data for steam id')
        
#     return player_steam_schema.load(steam_player_data)

# def get_friends_list(steam_id):
#     friends_list = steam_api.get_friend_list(steam_id)
#     friends_list = friends_list['friendslist']['friends']
#     steam_id_list = []
#     for friend in friends_list:
#         steam_id_list.append(friend['steamid'])
#     return steam_id_list
        