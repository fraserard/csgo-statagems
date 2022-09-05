from sqlalchemy.orm import joinedload

from app import db
from app.models import Team, TeamPlayer


def get_by_team_hash(team_hash: str) -> Team:
    return (
        Team.query.options(joinedload(Team.members).joinedload(TeamPlayer.player))
        .filter_by(team_hash=team_hash)
        .first()
    )


def get_by_player_ids(player_ids: set[int]) -> Team | None:
    team_hash = create_team_hash(player_ids)
    return (
        Team.query.options(joinedload(Team.members).joinedload(TeamPlayer.player))
        .filter_by(team_hash=team_hash)
        .first()
    )


def create_team(team_hash: str) -> Team:

    team = Team()
    team.team_hash = team_hash

    # create each team_player, x5
    for player_id in deconstruct_team_hash(team_hash):
        new_team_player = TeamPlayer()
        new_team_player.player_id = player_id

        team.members.append(new_team_player)

    return team


def create_team_from_players(player_ids: set[int]) -> Team:

    team = Team()
    team.team_hash = create_team_hash(player_ids)

    # create each team_player, x5
    for player_id in player_ids:
        new_team_player = TeamPlayer()
        new_team_player.player_id = player_id

        team.members.append(new_team_player)

    return team


def create_team_hash(player_ids: set[int]) -> str:
    """Returns a unique team hash from a set of player ids"""

    sorted_member_ids = sorted(player_ids)
    return "_".join(str(member_id) for member_id in sorted_member_ids)


def deconstruct_team_hash(team_hash: str) -> list[int]:
    """Returns a list of player ids from a team_hash"""

    return [int(player_id) for player_id in team_hash.split("_")]
