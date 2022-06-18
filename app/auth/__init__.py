
    
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