import os

STEAM_API_KEY = os.getenv('STEAM_API_KEY')
ADMIN_STEAM_ID = int(os.getenv('ADMIN_STEAM_ID'))
WEBSITE_URL = os.getenv('WEBSITE_URL')

STEAM_OPENID_SERVER = 'https://steamcommunity.com/openid/login'
OPENID_URL_PARAMS = {
    'openid.ns': 'http://specs.openid.net/auth/2.0',
    'openid.mode': 'checkid_setup',
    'openid.identity': 'http://specs.openid.net/auth/2.0/identifier_select',
    'openid.claimed_id': 'http://specs.openid.net/auth/2.0/identifier_select',
    'openid.return_to': f'{WEBSITE_URL}/auth/login/init',
    'openid.realm': WEBSITE_URL
}
STEAM_CLAIMED_ID_URL = 'https://steamcommunity.com/openid/id/' # openid identity returned like "https://steamcommunity.com/openid/id/{STEAM_ID64}"
