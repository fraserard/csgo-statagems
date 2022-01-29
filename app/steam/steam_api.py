import requests
from flask import current_app
class SteamAPIError(Exception):
    pass

class SteamAPI():
    
        
    def get_player_summaries(self, steam_id):
        """
        performs request for ISteamUser/GetPlayerSummaries. 
        :return: json response
        :more info: https://partner.steamgames.com/doc/webapi/ISteamUser#GetPlayerSummaries
        """
        _API_KEY = current_app.config["STEAM_API_KEY"]
        response = requests.get(f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={_API_KEY}&steamids={steam_id}')
        if response.status_code == 403: 
            raise SteamAPIError('403 error accessing steam api. invalid steam api key.')
        return response.json()
    
#     def get_friend_list(self, steam_id):
#         response = requests.get(f'https://api.steampowered.com/ISteamUser/GetFriendList/v1/?key={self._API_KEY}&steamid={steam_id}')
        
#         return response.json()

