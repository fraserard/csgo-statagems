from datetime import datetime, timedelta

from flask import Blueprint, current_app
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    get_jwt,
    set_access_cookies
)

from app.models import Player
from app import jwt

# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(jwt_header, jwt_data):
    identity = jwt_data["id"]
    player = Player.query.filter_by(id=identity).one_or_none()
    if not player: return None
    
    
# @jwt.token_in_blocklist_loader
# def is_token_revoked(jwt_header, jwt_payload):
#     jti = jwt_payload["jti"]
#     # get Player
#     # check if token exists
#     # check if token expired (revoked)
#     token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
#     return token is not None  
  
# https://flask-jwt-extended.readthedocs.io/en/stable/refreshing_tokens/
# @current_app.after_request
# def refresh_expiring_jwts(response):
#     try:
#         exp_timestamp = get_jwt()["exp"]
#         now = datetime.utcnow()
#         target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
#         if target_timestamp > exp_timestamp:
#             access_token = create_access_token(identity=get_jwt_identity())
#             set_access_cookies(response, access_token)
#         return response
#     except (RuntimeError, KeyError):
#         # Case where there is not a valid JWT. Just return the original respone
#         return response