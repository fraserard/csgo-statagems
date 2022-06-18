
from sqlalchemy.orm import joinedload

from app.models import Match, MatchPlayer, MatchTeam


def get_matches(player_id: int) -> list["Match"]:
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
