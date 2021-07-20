from flask import redirect, request, make_response
from flask.wrappers import Response
from flask_jwt_extended.utils import unset_jwt_cookies
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from urllib import parse
import requests
from flask_jwt_extended import create_access_token
import logging

from ..models.player import Player
from ..extensions import db
from ..steam_api_key import STEAM_API_KEY
from ..schemas.player_schemas import player_schema

#CONSTANTS
STEAM_OPENID_SERVER = 'https://steamcommunity.com/openid/login'
OPENID_URL_PARAMS = {
    'openid.ns': 'http://specs.openid.net/auth/2.0',
    'openid.mode': 'checkid_setup',
    'openid.identity': 'http://specs.openid.net/auth/2.0/identifier_select',
    'openid.claimed_id': 'http://specs.openid.net/auth/2.0/identifier_select',
    'openid.return_to': 'http://127.0.0.1:5000/api/login/init',
    'openid.realm': 'http://127.0.0.1:5000'
}
STEAM_ID_URL = 'https://steamcommunity.com/openid/id/'

class LoginApi(Resource):
    def get(self):
        
        return redirect(f'{STEAM_OPENID_SERVER}?{parse.urlencode(OPENID_URL_PARAMS)}')

class LoginInit(Resource):
    def get(self):        
        data = request.args
        
        if data['openid.mode'] == 'error' or data['openid.mode'] == None:
            logging.error("steam open id auth error")
            return {'msg': 'error', 'description': 'steam open id auth error'}

        sid = data['openid.claimed_id'].lstrip(STEAM_ID_URL) # steamid64

        if sid is None:
            logging.error(f"steam id not found after openid login")
            return {'msg': 'error', 'description': 'steam open id auth error'}
        
        player_data = requests.get(f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={STEAM_API_KEY}&steamids={sid}').json()
        player_data = player_data['response']['players'][0]

        if player_data is None:
            logging.error(f"error accessing steam api with steamid {sid}")
            return {'msg': 'error', 'description': 'error accessing steam api'}

        player = Player.query.filter_by(steam_id=sid).first()

        if player is None: # if new registration, make new player
            try:
                new_player = Player(
                    steam_id = player_data['steamid'],
                    username = player_data['personaname'], 
                    name = data['realname'],
                    profile_pic_url = data['avatarfull'])
                db.session.add(new_player)
                db.session.commit()
                player = Player.query.filter_by(steam_id=sid).first()
            except:
                logging.error(f"error creating user {player.id} during login")
                return {'msg': 'error', 'description': 'adding new player failed'}
            
        else: 
            try:
                if player.username != player_data['personaname']:
                    player.username = player_data['personaname']
                if player.name != player_data['realname']:
                    player.name = player_data['realname']
                if player.profile_pic_url != player_data['avatarfull']:
                    player.profile_pic_url = player_data['avatarfull']
                db.session.commit()
            except:
                logging.error(f"error updating user {player.id} during login")
                return {'msg': 'error', 'description': 'updating existing player failed'}

        # create jwt
        access_token = create_access_token(identity=player.id) 
        logging.info(f"created jwt for user {player.id}")

        return {'jwt':access_token, 'player': player_schema.dump(player)}

class LogoutApi(Resource):
    @jwt_required()
    def get(self):
        
        unset_jwt_cookies(make_response())
        return {'msg': 'logout'} # redirect to landing page
    

