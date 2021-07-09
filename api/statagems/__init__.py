from flask import Flask
from flask_restful import Api

from statagems.models.__init__ import db
from statagems.schemas.__init__ import ma
from statagems.routes.__init__ import initialize_routes

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='mysql://root:admin@localhost:3306/statagems',
        #SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
        SQLALCHEMY_TRACK_MODIFICATIONS='false',
    )
    
    initialize_extensions(app)

    return app

def initialize_extensions(app):
    db.init_app(app)
    ma.__init__(app)
    api = Api(app)
    initialize_routes(api)

