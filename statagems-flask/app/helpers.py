import re


def is_valid_steam_id(steam_id) -> bool:
    """Checks if input is in 64 bit SteamId format."""

    steam_id = str(steam_id)
    if re.search("^(7656[0-9]{13})$", steam_id) is None or steam_id is None:
        return False
    return True

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

# def get_friends_list(steam_id):
#     friends_list = steam_api.get_friend_list(steam_id)
#     friends_list = friends_list['friendslist']['friends']
#     steam_id_list = []
#     for friend in friends_list:
#         steam_id_list.append(friend['steamid'])
#     return steam_id_list

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
