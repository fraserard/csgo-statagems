from flask import current_app as app
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import get_jwt, create_access_token, get_jwt_identity, set_access_cookies

# https://flask-jwt-extended.readthedocs.io/en/stable/refreshing_tokens/

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response