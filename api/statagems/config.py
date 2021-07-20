"""Default configuration

Use env var to override
"""
import os
from datetime import timedelta

ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_COOKIE_SECURE = ENV != "development"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
