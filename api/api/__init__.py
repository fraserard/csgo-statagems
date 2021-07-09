from flask import Flask
from flask_restful import Api
from .route import initialize_routes


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='mysql://root:admin@localhost:3306/statagems',
        #SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
        SQLALCHEMY_TRACK_MODIFICATIONS='false'
    )

    from .model import db
    db.init_app(app)
    
    from .schemas import ma
    ma.__init__(app)
    
    api = Api(app)
    initialize_routes(api)

    return app


