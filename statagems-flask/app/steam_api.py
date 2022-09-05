import requests
from flask import current_app


class SteamAPIError(Exception):
    pass


class SteamAPI:
    def get_player_summaries(self, steam_id):
        """
        performs request for ISteamUser/GetPlayerSummaries.
        :steam_id: single steamId or list of steamIds
        :return: json response
        :more info: https://partner.steamgames.com/doc/webapi/ISteamUser#GetPlayerSummaries
        """
        _API_KEY = current_app.config["STEAM_API_KEY"]
        response = requests.get(
            f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={_API_KEY}&steamids={steam_id}"
        )
        if response.status_code == 403:
            raise SteamAPIError("Steam API Error")
        try:
            response = response.json()
        except requests.exceptions.JSONDecodeError as e:
            raise SteamAPIError("Steam API Error")

        return response["response"]["players"]

    def get_friend_list(self, steam_id):
        _API_KEY = current_app.config["STEAM_API_KEY"]
        response = requests.get(
            f"https://api.steampowered.com/ISteamUser/GetFriendList/v1/?key={_API_KEY}&steamid={steam_id}"
        )

        if response.status_code == 403:
            raise SteamAPIError("403 error accessing steam api. invalid steam api key.")

        response = response.json()
        return response["friendslist"]["friends"]
