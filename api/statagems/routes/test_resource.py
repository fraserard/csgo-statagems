import logging
from flask_restful import Resource
import requests
from sqlalchemy.orm import load_only
from ..constants import STEAM_API_KEY, ADMIN_STEAM_ID
from ..models.player import Player
from ..models.admin import Admin
from ..extensions import db

class TestPopulatePlayers(Resource): # /test/populate_players
    def get(self):
        # recreates database, then populates with Players from ADMIN_STEAM_ID's Steam Friends List
        db.drop_all()
        db.create_all()

        resp = requests.get(f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={STEAM_API_KEY}&steamids={ADMIN_STEAM_ID}')
        admin_data = resp.json()
        admin_data = admin_data['response']['players'][0]
        faffers = Admin(
            steam_id = admin_data['steamid'],
            username = admin_data['personaname'],
            avatar_hash = admin_data['avatarhash'],
            permission_clearance = 0,
            acct_type= 'admin'
        )
        if 'realname' in admin_data:
                    faffers.name = (admin_data['realname'])[:32]
        db.session.add(faffers)

        resp = requests.get(f'https://api.steampowered.com/ISteamUser/GetFriendList/v1/?key={STEAM_API_KEY}&steamid={ADMIN_STEAM_ID}')
        friends_list = resp.json()
        friends_list = friends_list['friendslist']['friends']
        steamid_list = []
        for f in friends_list:
            steamid_list.append(f['steamid'])

        resp = requests.get(f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={STEAM_API_KEY}&steamids={steamid_list}')
        players_data = resp.json()
        players_data = players_data['response']['players']

        for p in players_data:
            logging.error(p)
            player = Player.query.options(load_only('steam_id', 'username', 'name', 'avatar_hash')).filter_by(steam_id=p['steamid']).first()
            if player is None: # if new registration, make new player from steam api data
                new_player = Player(
                steam_id = p['steamid'],
                username = p['personaname'], 
                avatar_hash = p['avatarhash'] )
                if 'realname' in p:
                    new_player.name = (p['realname'])[:32]
            
                db.session.add(new_player)
            else: # if player exists, update from steam api data
                if player.username != p['personaname']:
                    player.username = p['personaname']
                if 'realname' in p:
                    if player.name != p['realname']:
                        player.name = (p['realname'])[:32]
                if player.avatar_hash != p['avatarhash']:
                    player.avatar_hash = p['avatarhash']
                
        
        db.session.commit()
        return {'msg': 'nice job'} 