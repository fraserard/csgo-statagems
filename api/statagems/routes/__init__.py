from api.statagems.routes.matches_resource import MatchesApi
from .players_resource import PlayerApi, PlayersApi, PlayerSelf
from .auth_resource import LoginApi, LoginInit, LogoutApi
# from .admin_resource import AdminPlayers, AdminPlayer, AdminMatch, AdminMatches
from .test_resource import TestPopulatePlayers
def initialize_routes(api):
    # TESTING
    api.add_resource(TestPopulatePlayers, '/test/populate_players')

    # logging in / registration
    api.add_resource(LoginApi, '/auth/login')
    api.add_resource(LoginInit, '/auth/login/init')
    api.add_resource(LogoutApi, '/auth/logout')

    # players - general user
    api.add_resource(PlayersApi, '/api/players')
    api.add_resource(PlayerApi, '/api/players/<id>')
    api.add_resource(PlayerSelf, '/api/me')

    # groups
    api.add_resource(GroupsApi, '/api/groups')
    api.add_resource(GroupApi, '/api/groups/<gid>')

    # group player
    api.add_resource(GroupPlayerApi, '/api/groups/<gid>/<pid>')

    # matches for group
    api.add_resource(MatchesApi, '/api/matches')
    
    # admin
    # api.add_resource(AdminPlayers, '/admin/players')
    # api.add_resource(AdminPlayer, '/admin/players/<id>')
    # api.add_resource(AdminMatches, '/admin/matches')
    # api.add_resource(AdminMatch, '/admin/matches/<id>')
    # api.add_resource(AdminGroups, '/admin/groups')
    # api.add_resource(AdminGroup, '/admin/groups/<id>')
    # api.add_resource(AdminAdmins, '/admin/admins')
    # api.add_resource(AdminAdmin, '/admin/admins/<id>')

    # friends
    # api.add_resource(FriendsApi, '/api/friends')
    # api.add_resource(FriendApi, '/api/friends/<id>')
    # api.add_resource(FriendRequestsApi, '/api/friendreqs')
    # api.add_resource(FriendRequestApi, '/api/friendreqs/<id>')





    
