from dataclasses import dataclass
from datetime import datetime

from app import db
from app.models import Match, MatchPlayer, MatchTeam, TeamSides
from app.services import aggregates, teams
from sqlalchemy import desc
from sqlalchemy.orm import joinedload


def get_match(match_id: int) -> Match:
    """Gets a single match by id."""
    return (
        Match.query.options(
            joinedload(Match.map), joinedload(Match.teams).joinedload(MatchTeam.players)
        )
        .filter_by(id=match_id)
        .first()
    )

def get_recent_match() -> Match:
        return (
        Match.query.options(
            joinedload(Match.map), joinedload(Match.teams).joinedload(MatchTeam.players)
        )
        .order_by(desc(Match.date_played))
        .first()
    )

def get_matches() -> list[Match]:
    """Gets all matches, ordered by most recent."""
    return (
        Match.query.options(
            joinedload(Match.map), joinedload(Match.teams).joinedload(MatchTeam.players)
        )
        .order_by(desc(Match.date_played))
        .all()
    )


@dataclass
class NewMatchPlayer:
    player_id: int
    kills: int
    assists: int
    deaths: int


@dataclass
class NewMatchTeam:
    start_side: TeamSides
    rounds_won: int
    rounds_lost: int
    players: list[NewMatchPlayer]
    captain_id: int | None
    team_hash: str


@dataclass
class NewMatch:
    map_id: int
    team1: NewMatchTeam
    team2: NewMatchTeam
    date_played: datetime


def process_match(match_data: NewMatch) -> Match:
    """
    Creates a new match and updates all running totals.
    """

    match = Match(map_id=match_data.map_id, date_played=match_data.date_played)

    match.teams.append(process_match_team(match_data.team1, date_played=match_data.date_played))
    match.teams.append(process_match_team(match_data.team2, date_played=match_data.date_played))

    return match


def process_match_team(new_match_team: NewMatchTeam, date_played: datetime) -> MatchTeam:
    team = teams.get_by_team_hash(new_match_team.team_hash)

    if not team:
        team = teams.create_team(new_match_team.team_hash)
        db.session.add(team)
        db.session.flush()
        # fetch team again to get players
        team = teams.get_by_team_hash(new_match_team.team_hash)

    match_team = MatchTeam(
        start_side=new_match_team.start_side,
        captain_id=new_match_team.captain_id,
        rounds_won=new_match_team.rounds_won,
        team=team,
    )

    aggregates.update_group_aggregates(team, new_match_team)

    # sort by player_id
    new_match_team.players = sorted(
        new_match_team.players, key=lambda player: player.player_id
    )
    team.members = sorted(team.members, key=lambda player: player.player_id)

    # new_match_team.players and team.members MUST BE SORTED
    for player_input, team_player in zip(new_match_team.players, team.members):

        aggregates.update_individual_aggregates(team_player, player_input)

        aggregates.update_individual_aggregates(team_player.player, player_input)
        aggregates.update_group_aggregates(team_player.player, new_match_team)

        if new_match_team.captain_id is not None:
            is_captain = new_match_team.captain_id == player_input.player_id
            aggregates.update_times_captain(team_player, is_captain)
            aggregates.update_times_captain(team_player.player, is_captain)

        team_player.player.last_seen = date_played

        # TODO Update player's steam data?

        new_match_player = MatchPlayer(
            player_id=player_input.player_id,
            kills=player_input.kills,
            assists=player_input.assists,
            deaths=player_input.deaths,
            steam_username=team_player.player.steam_username,
            steam_avatar_hash=team_player.player.steam_avatar_hash,
        )
        match_team.players.append(new_match_player)
    return match_team


def remove_match(match_id: int) -> bool:
    return False
