import strawberry
from app import models
from app.api.players.types import Player, PlayerList, SteamID


@strawberry.type
class Query:
    @strawberry.field(description="Get a list of all players.")
    def players(self) -> list["PlayerList"]:
        players_data: list["models.Player"] = models.Player.query.all()
        return [PlayerList.marshal(player_data) for player_data in players_data]

    @strawberry.field(description="Get a single player by their SteamID.")
    def player(self, steam_id: SteamID) -> "Player":
        player_data = models.Player.query.filter_by(steam_id=int(steam_id)).first()
        return Player.marshal(player_data)

    # self: 'Player' = strawberry.field(resolver=get_self)
    # topNutter: 'Player'
