from flask import request, make_response
from flask_jwt_extended.utils import set_access_cookies, unset_jwt_cookies
from flask_jwt_extended.view_decorators import jwt_required
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from urllib import parse
import logging, requests

from ..extensions import db
from ..constants import WEBSITE_URL, STEAM_OPENID_SERVER, OPENID_URL_PARAMS, STEAM_CLAIMED_ID_URL
from ..helpers.auth_helper import login_create_update_player

class LoginApi(Resource): # /auth/login
    def get(self):
        res = make_response()
        res.status_code=302 # add proper headers for Steam OpenID 2.0 server
        res.headers.add_header('Location', f'{STEAM_OPENID_SERVER}?{parse.urlencode(OPENID_URL_PARAMS)}')
      
        return res # redirect to steam login page

class LoginInit(Resource): # /auth/login/init  - steam openid redirects here
    def get(self):
        res = make_response()
        try:
            params = request.args # get url params
            logging.error(params)
            if params['openid.mode'] == 'error' or params['openid.claimed_id'] == None:
                raise Exception('steam open id auth error')

            # VALIDATE STEAM OPENID RESPONSE ID
            params = params.to_dict()
            params['openid.mode'] = 'check_authentication' # change mode from id_res to check_auth
            logging.error(params)
            resp = requests.post(f'{STEAM_OPENID_SERVER}?{parse.urlencode(params)}')
            if 'is_valid:true' not in resp.text:
                raise Exception('steam openid auth not valid')

            sid = int(params['openid.claimed_id'].lstrip(STEAM_CLAIMED_ID_URL)) # steamid64
            
            player_data = login_create_update_player(sid)
            
            db.session.commit()

            # create jwt, identity is dict based off player_schema
            access_token = create_access_token(identity=player_data) 
            logging.info(f'created jwt for user { player_data["id"] }')
      
            set_access_cookies(res, access_token, max_age=3600)        
            res.headers.add_header('Location', f'{WEBSITE_URL}/player/{player_data["id"]}')
        except Exception as e:
            res.headers.add_header('Location', f'{WEBSITE_URL}/error')
            logging.exception(f'{LoginInit.__name__}', e)
        except BaseException as e:
            res.headers.add_header('Location', f'{WEBSITE_URL}/error')
            logging.critical(f'{LoginInit.__name__} BaseException. {e}')
        finally:
            res.status_code=302
            # res.delete_cookie('steam_oid_session')
            
        return res # redirect to profile page with jwt cookies

class LogoutApi(Resource): # /auth/logout
    @jwt_required()
    def get(self):
        res = make_response()
        try:   
            unset_jwt_cookies(res)
            res.status_code=200
        except:
            res.status_code=301
        return res
    

