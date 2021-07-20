from flask import Flask
from .extensions import db, ma, migrate, api, jwt
from .routes import initialize_routes

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object("statagems.config")
    
    initialize_extensions(app)
    initialize_routes(api)

    return app

def initialize_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    jwt.init_app(app)

# @jwt.token_in_blocklist_loader # checks if refresh token revoked
# def check_if_token_is_revoked(jwt_header, jwt_payload):
#     jti = jwt_payload["jti"]
#     return __name__.models.TokenBlocklist.is_jti_blacklisted(jti)
