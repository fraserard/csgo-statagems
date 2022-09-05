from sqlalchemy.orm import joinedload

from app.models import Match, MatchPlayer, MatchTeam, Player
from app.services import teams


def get_matches(player_id: int) -> list[Match]:
    return (
        Match.query.options(
            joinedload(Match.map), joinedload(Match.teams).joinedload(MatchTeam.players)
        )
        .order_by(Match.date_played)
        .join(MatchTeam)
        .join(MatchPlayer)
        .filter(MatchPlayer.player_id == player_id)
        .all()
    )


def get_players(player_ids: set[int]) -> list[Player]:
    return Player.query(Player).filter(Player.id.in_(player_ids)).all()  # type: ignore


def get_players_by_team_hash(team_hash: str) -> list[Player]:
    return (
        Player.query(Player)
        .filter(Player.id.in_(teams.deconstruct_team_hash(team_hash)))  # type: ignore
        .all()
    )
