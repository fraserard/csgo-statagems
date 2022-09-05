import os

from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()


def create_app(config_class=Config):
    app = Flask(__name__, static_folder="../../statagems-react/dist")
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    from app.auth.views import auth_bp

    app.register_blueprint(auth_bp)

    from app.api.schema import FlaskGraphQLView, schema

    app.add_url_rule(
        "/graphql",
        view_func=FlaskGraphQLView.as_view("graphql", schema=schema, graphiql=True),
    )

    from app import cli

    cli.register(app)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def serve(path):
        if path != "" and os.path.exists(f"{app.static_folder}/{path}"):
            return send_from_directory(app.static_folder, path)  # type: ignore
        else:
            return send_from_directory(app.static_folder, "index.html")  # type: ignore

    return app
