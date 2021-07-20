from .players_resource import PlayerApi, PlayersApi
from .auth_resource import LoginApi, LoginInit, LogoutApi

def initialize_routes(api):
    # logging in / registration
    api.add_resource(LoginApi, '/api/login')
    api.add_resource(LoginInit, '/api/login/init')
    api.add_resource(LogoutApi, '/api/logout')
    
    api.add_resource(PlayersApi, '/api/players')
    api.add_resource(PlayerApi, '/api/players/<id>')


    
