from flask import Flask
from .extensions import db, ma, migrate, api, jwt
from .routes.__init__ import initialize_routes

def create_app():
    # create and configure the app
    app = Flask('statagems')
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

# set in env
if __name__ == 'statagems':
    create_app()
