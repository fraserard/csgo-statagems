import datetime
import os
from datetime import timedelta

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    # DEVELOPMENT CONFIG
    FLASK_DEBUG = True
    SQLALCHEMY_ECHO = False

    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_TOKEN_LOCATION = "cookies"
    JWT_ACCESS_COOKIE_NAME = "statagems_token"
    JWT_ACCESS_CSRF_COOKIE_NAME = "statagems_csrf"
    JWT_SESSION_COOKIE = False
    JWT_COOKIE_SECURE = True
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=8)
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_COOKIE_SAMESITE = "Strict"

    STEAM_API_KEY = os.getenv("STEAM_API_KEY")
    ADMIN_STEAM_ID = os.getenv("ADMIN_STEAM_ID")
    WHITELIST_STEAM_IDS = str(os.getenv("WHITELIST_STEAM_IDS")).split(",")

    WEBSITE_URL = os.getenv("WEBSITE_URL")
    SERVER_URL = os.getenv("SERVER_URL")
    # Steam's OpenID server
    OPENID_SERVER = "https://steamcommunity.com/openid/login"

    OPENID_URL_PARAMS = {
        "openid.ns": "http://specs.openid.net/auth/2.0",
        "openid.mode": "checkid_setup",
        "openid.identity": "http://specs.openid.net/auth/2.0/identifier_select",
        "openid.claimed_id": "http://specs.openid.net/auth/2.0/identifier_select",
        "openid.return_to": f'{WEBSITE_URL}/auth/steam',
        "openid.realm": WEBSITE_URL,
    }
    OPENID_RESPONSE_REFERRER = "https://steamcommunity.com"

    STEAM_API_COOLDOWN = timedelta(days=0, hours=1, minutes=0)
