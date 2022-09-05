from datetime import datetime
from urllib.parse import urlencode

import requests
from flask import Blueprint, current_app, jsonify, make_response, request
from flask_jwt_extended import create_access_token, set_access_cookies

from app import db
from app.models import Player

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["GET"])
def login():
    response = make_response()
    response.status_code = 302

    STEAM_OPENID_SERVER = current_app.config["OPENID_SERVER"]
    OPENID_URL_PARAMS = current_app.config["OPENID_URL_PARAMS"]

    # add proper headers for Steam OpenID 2.0 server
    response.headers.add_header(
        "Location", f"{STEAM_OPENID_SERVER}?{urlencode(OPENID_URL_PARAMS)}"
    )

    return response  # redirect to steam login page


class OpenIDError(Exception):
    pass


@auth_bp.route("/steam", methods=["GET"])
def auth_steam():
    response = make_response()
    response.status_code = 302

    WEBSITE_URL = current_app.config["WEBSITE_URL"]

    try:
        # VALIDATE STEAM OPENID RESPONSE ID
        params = request.args.to_dict()  # not needed? **
        params[
            "openid.mode"
        ] = "check_authentication"  # change openid.mode from id_res -> check_authentication

        STEAM_OPENID_SERVER = current_app.config["OPENID_SERVER"]
        # send validation request to steam openid
        validation_response = requests.post(
            f"{STEAM_OPENID_SERVER}?{urlencode(params)}"
        )

        # validation_response_json = validation_response.json()
        # if validation_response_json['is_valid'] != True:
        #     raise OpenIDError('Steam OpenID error.')

        if "is_valid:true" not in validation_response.text:
            raise OpenIDError("Steam OpenID error.")

        # open_id.claimed_id like "https://steamcommunity.com/openid/id/{STEAM_ID}"
        # extracting STEAM_ID from open_id.claimed_id
        steam_id = params["openid.claimed_id"].split("/id/").pop()  # steamid64

        # accessing_player = Player.query.options(load_only('id', 'role')).filter_by(steam_id=steam_id).first()
        accessing_player = Player.get_by_steam_id(steam_id)

        # If None that means Player is not whitelisted.
        if accessing_player is None:  # Not authorized
            raise OpenIDError("Not authorized.")

        # create jwt
        access_token = create_access_token(
            identity={
                "player_id": accessing_player.id,
                "role": accessing_player.role.name,
                "steam_username": accessing_player.steam_username,
                "steam_avatar_hash": accessing_player.steam_avatar_hash,
            }
        )

        set_access_cookies(response, access_token)

        # if existing Player and last seen over a day ago, update with steam data
        # elif accessing_player: # add logic to only call steamAPI after certain time
        accessing_player.refresh_steam_data()
        accessing_player.last_seen = datetime.utcnow()
        db.session.commit()

        # set redirect header to index
        response.headers.add_header("Location", f"{WEBSITE_URL}")
    except OpenIDError as e:
        response.headers.add_header("Location", f"{WEBSITE_URL}/error")

    return response  # redirect to profile page with jwt cookies
