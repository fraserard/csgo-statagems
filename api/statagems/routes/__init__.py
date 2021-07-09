from .players_resource import PlayerApi, PlayersApi

def initialize_routes(api):
    api.add_resource(PlayersApi, '/api/players')
    api.add_resource(PlayerApi, '/api/players/<id>')

