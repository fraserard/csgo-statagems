import strawberry
from app import db, models
from app.api.players.types import LoggedInUser, Player, SteamID
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import CSRFError, NoAuthorizationError
from jwt import ExpiredSignatureError
from strawberry.types import Info


@strawberry.type
class Query:
    @strawberry.field(description="Get a list of all players.")
    def players(self) -> list[Player]:
        players_data: list[models.Player] = (
            db.session.query(models.Player)
            .filter(models.Player.role != models.PlayerRoles.REMOVED)
            .all()
        )

        return [Player.marshal(player_data) for player_data in players_data]

    @strawberry.field(description="Get a single player by their SteamID.")
    def player(self, steam_id: SteamID) -> Player:
        player_data = models.Player.query.filter_by(steam_id=int(steam_id)).first()
        return Player.marshal(player_data)

    @strawberry.field(description="Get a list of all users.")
    def users(self) -> list[Player]:
        players_data: list[models.Player] = (
            db.session.query(models.Player)
            .order_by(
                models.Player.role,
                models.Player.username,
            )
            .all()
        )
        return [Player.marshal(player_data) for player_data in players_data]

    @strawberry.field()
    def current_user(self, info: Info) -> LoggedInUser | None:
        try:
            jwt = verify_jwt_in_request(optional=True)
            if jwt is None:
                return None

            jwt_header, jwt_data = jwt

        except (CSRFError, NoAuthorizationError, ExpiredSignatureError):
            return None

        jwt_data = jwt_data["sub"]
        user: models.Player = (
            db.session.query(models.Player).filter_by(id=jwt_data["player_id"]).scalar()
        )
        return LoggedInUser.marshal(model=user)
