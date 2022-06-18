from sqlalchemy.orm import joinedload

from app.models import Team, TeamPlayer
from app import db


def get_by_team_hash(team_hash: str) -> Team:
    return (
        Team.query.options(joinedload(Team.members).joinedload(TeamPlayer.player))
        .filter_by(team_hash=team_hash)
        .first()
    )


def add_team(player_ids: list[int]) -> Team:
    
    team = Team()
    team.team_hash = create_team_hash(player_ids)

    # create each team_player, x5
    for player_id in player_ids:
        new_team_player = TeamPlayer()
        new_team_player.player_id = player_id
        
        team.members.append(new_team_player)

    db.session.add(team)
    return team


def create_team_hash(player_ids: list[int]) -> str:
    """Returns a unique team hash from a list of player ids"""

    sorted_member_ids = sorted(player_ids)
    return "_".join(str(member_id) for member_id in sorted_member_ids)
