from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
        SQLALCHEMY_TRACK_MODIFICATIONS='false'
    )

    from api.model import db
    db.init_app(app)

    from . import route
    app.register_blueprint(route.main_bp)

    return app




  



