import requests
from urllib.parse import urlencode

from flask import request, jsonify, Blueprint, current_app, make_response
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
    set_access_cookies
)

from app.models import Player
from app import db
from app.steam.steam_helpers import get_player_from_steam, is_valid_steam_id


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["GET"])
def login():
  response = make_response()
  response.status_code = 302
        
  STEAM_OPENID_SERVER = current_app.config['OPENID_SERVER']
  OPENID_URL_PARAMS = current_app.config['OPENID_URL_PARAMS']
  
  # add proper headers for Steam OpenID 2.0 server
  response.headers.add_header('Location', f'{STEAM_OPENID_SERVER}?{urlencode(OPENID_URL_PARAMS)}')
  
  return response # redirect to steam login page

class OpenIDError(Exception):
    pass
  
@auth_bp.route("/steam", methods=["GET"])
def auth_steam():
    response = make_response()
    response.status_code = 302
    
    WEBSITE_URL = current_app.config['WEBSITE_URL']

    try:
        # if request.referrer != 'https://steamcommunity.com':
        #     raise OpenIDError('wrong referrer')
        
        params = request.args # get url params
        if params['openid.mode'] == 'error' or params['openid.claimed_id'] == None:
            raise OpenIDError('steam open id auth error')
        
        # VALIDATE STEAM OPENID RESPONSE ID
        params = params.to_dict() # not needed? **
        params['openid.mode'] = 'check_authentication' # change openid.mode from id_res -> check_authentication
        
        STEAM_OPENID_SERVER = current_app.config['OPENID_SERVER']
        # send validation request to steam openid
        validation_response = requests.post(f'{STEAM_OPENID_SERVER}?{urlencode(params)}')
        if 'is_valid:true' not in validation_response.text:
            raise OpenIDError('steam openid auth invalid')
        
        # open_id.claimed_id like "https://steamcommunity.com/openid/id/{STEAM_ID}"
        # extracting steam_id from claimed_id
        steam_id = int(params['openid.claimed_id'].split('/id/').pop()) # steamid64
  
        if not is_valid_steam_id(steam_id):
            raise OpenIDError('steam id format incorrect')
    
        accessing_player = Player.get_by_steam_id(steam_id)
        
        # if new user, create Player with steam data
        if accessing_player is None: 
            new_player: Player = get_player_from_steam(steam_id)
            db.session.add(new_player)
            db.session.commit()
                
        # if existing Player and last seen over a day ago, update with steam data
        elif accessing_player: # add logic to only call steamAPI after certain time
            new_player: Player = get_player_from_steam(steam_id)
            # update fields
            accessing_player.steam_username = new_player.steam_username
            accessing_player.steam_avatar_hash = new_player.steam_avatar_hash
            accessing_player.steam_real_name = new_player.steam_real_name
            accessing_player.last_fetched_steam = new_player.last_fetched_steam
            db.session.commit()

        # create jwt
        access_token = create_access_token(identity=accessing_player.id) 
        set_access_cookies(response, access_token)

        # set redirect header to player's profile       
        response.headers.add_header('Location', f'{WEBSITE_URL}/player/{accessing_player.steam_id}')
    except OpenIDError:
        response.headers.add_header('Location', f'{WEBSITE_URL}/openid_error')
        
    return response # redirect to profile page with jwt cookies  
  
@auth_bp.route("/revoke_access", methods=["DELETE"])
@jwt_required()
def revoke_access_token():
    jti = get_jwt()["jti"]
    user_identity = get_jwt_identity()
    # revoke token
    # set Player.token_expiry to the past
    # if Player.token_expiry is in past, token effectively revoked
    return jsonify({"message": "token revoked"}), 200




