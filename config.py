from datetime import timedelta
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # DEVELOPMENT CONFIG
    FLASK_DEBUG = True
    SQLALCHEMY_ECHO = True
    
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # JWT_TOKEN_LOCATION = "cookies"
    # JWT_COOKIE_SECURE = True
    # JWT_ACCESS_TOKEN_EXPIRES = 3600 # 3600s, 1hr
    # JWT_COOKIE_CSRF_PROTECT = True
    # JWT_CSRF_IN_COOKIES = True
    # JWT_COOKIE_SAMESITE = 'Strict'
    # JWT_CSRF_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    STEAM_API_KEY = os.getenv('STEAM_API_KEY')
    ADMIN_STEAM_ID = os.getenv('ADMIN_STEAM_ID')

    WEBSITE_URL = 'http://127.0.0.1:5000'

    OPENID_SERVER = 'https://steamcommunity.com/openid/login'
    OPENID_RETURN_TO = WEBSITE_URL + '/auth/steam'
    OPENID_URL_PARAMS = {
        'openid.ns': 'http://specs.openid.net/auth/2.0',
        'openid.mode': 'checkid_setup',
        'openid.identity': 'http://specs.openid.net/auth/2.0/identifier_select',
        'openid.claimed_id': 'http://specs.openid.net/auth/2.0/identifier_select',
        'openid.return_to': OPENID_RETURN_TO,
        'openid.realm': WEBSITE_URL
    }
    OPENID_RESPONSE_REFERRER = 'https://steamcommunity.com'

    STEAM_API_COOLDOWN = timedelta(days=0, hours=1, minutes=0)