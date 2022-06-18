from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from sqlalchemy.orm import joinedload

from app import db
from app.models import Match, MatchPlayer, MatchTeam
from app.models.match_team import TeamSides
from app.services import aggregates, teams


def get_match(match_id: int) -> Match:
    """Gets a single match by id."""
    return (
        Match.query.options(
            joinedload(Match.map), joinedload(Match.teams).joinedload(MatchTeam.players)
        )
        .filter_by(id=match_id)
        .first()
    )


def get_matches() -> list["Match"]:
    """Gets all matches, ordered by most recent."""
    return (
        Match.query.options(
            joinedload(Match.map), joinedload(Match.teams).joinedload(MatchTeam.players)
        )
        .order_by(Match.date_played)
        .all()
    )



# @dataclass
# class NewMatchTeam:
#     start_side: TeamSides
#     rounds_won: int
#     rounds_lost: int
#     players: list["NewMatchPlayer"]
#     captain_id: int | None


# @dataclass
# class NewMatch:
#     map_id: int
#     team1: "NewMatchTeam"
#     team2: "NewMatchTeam"
#     date_played: datetime


# @dataclass
# class NewMatchPlayer:
#     player_id: int
#     kills: int
#     assists: int
#     deaths: int
#     mvps: int | None = None
#     score: int | None = None
#     adr: int | None = None

class NewMatchPlayer(Protocol):
    player_id: int
    kills: int
    assists: int
    deaths: int
    # mvps: int | None = None
    # score: int | None = None
    # adr: int | None = None


class NewMatchTeam(Protocol):
    start_side: TeamSides
    rounds_won: int
    rounds_lost: int
    players: list[NewMatchPlayer]
    captain_id: int | None


class NewMatch(Protocol):
    map_id: int
    team1: NewMatchTeam
    team2: NewMatchTeam
    date_played: datetime 


def add_match(new_match: NewMatch) -> Match:
    """
    Adds a new match and updates all running totals.
    """

    if not new_match.date_played:
        new_match.date_played = datetime.utcnow()

    match = Match(map_id=new_match.map_id)

    match.teams.append(add_match_team(new_match.team1))
    match.teams.append(add_match_team(new_match.team2))

    db.session.add(match)
    db.session.commit()

    return match


def add_match_team(new_match_team: NewMatchTeam):

    # create new MatchTeam
    match_team = MatchTeam(
        start_side=new_match_team.start_side,
        captain_id=new_match_team.captain_id,
        rounds_won=new_match_team.rounds_won,
    )

    # create team_hash from member_ids
    team_hash = teams.create_team_hash(
        [player.player_id for player in new_match_team.players]
    )

    team = teams.get_by_team_hash(team_hash)

    if not team:
        team = teams.add_team([player.player_id for player in new_match_team.players])
        db.session.flush()

    # TODO switch to team_hash instead of id
    match_team.team_id = team.id

    # update Team aggregate stats
    aggregates.update_group_aggregates(team, new_match_team)

    # sort by player_id
    new_match_team.players = sorted(new_match_team.players, key=lambda k: k.player_id)
    team.members = sorted(team.members, key=lambda k: k.player_id)

    # new_match_team.players and team.members MUST BE SORTED
    for player_input, team_player in zip(new_match_team.players, team.members):
        # TODO def add_match_player()

        # set is_captain helper bool
        is_captain = new_match_team.captain_id == player_input.player_id

        # update TeamPlayer aggregate stats
        aggregates.update_kills_assists_deaths(team_player, player_input, is_captain)

        # update Player aggregate stats
        aggregates.update_kills_assists_deaths(
            team_player.player, player_input, is_captain
        )
        aggregates.update_group_aggregates(team_player.player, new_match_team)

        # TODO Update player's steam data?

        new_match_player = MatchPlayer(
            player_id=player_input.player_id,
            kills=player_input.kills,
            assists=player_input.assists,
            deaths=player_input.deaths,
            # mvps=player_input.mvps,
            # score=player_input.score,
            # adr=player_input.adr,
            steam_username=team_player.player.steam_username,
            steam_avatar_hash=team_player.player.steam_avatar_hash,
        )
        match_team.players.append(new_match_player)
    return match_team


# def add_match(match_input: AddMatchInput):
#     """
#     Adds a new match and updates all running totals.
#     """

#     # add match
#     # add match_team for both teams
#     # add match_player for both teams
#     # update or add team for both teams
#     # update or add team_player for all 10 players
#     # update player for all 10 players

#     if not match_input.date_played:
#         match_input.date_played = datetime.utcnow()

#     new_match = Match(map_id=match_input.map_id)

#     # set rounds_lost for team1, team2 set at end of for loop
#     rounds_lost = match_input.team2.rounds_won

#     # for each team in the match, loop 2x
#     for match_team_input in [match_input.team1, match_input.team2]:

#         # create new MatchTeam
#         new_match_team = MatchTeam(
#             start_side=match_team_input.start_side.name,
#             captain_id=match_team_input.captain_id,
#             rounds_won=match_team_input.rounds_won,
#         )

#         # sort team_data.players by player_id
#         match_team_input.players = sorted(
#             match_team_input.players, key=lambda k: k.player_id
#         )

#         # list of member_ids, used for team_hash
#         member_ids = [player.player_id for player in match_team_input.players]

#         # create team_hash from member_ids
#         team_hash = teams.create_team_hash(member_ids)

#         team: "Team" = teams.get_by_team_hash(team_hash)

#         if not team:  # if Team does not exist, create
#             team = teams.add_team(
#                 match_team_input=match_team_input, team_hash=team_hash
#             )
#             db.session.flush()
#         else:
#             team.members = sorted(team.members, key=lambda k: k.player_id)

#         new_match_team.team_id = team.id

#         # update Team aggregate stats
#         aggregates.update_team_aggregates(team, match_team_input, rounds_lost)

#         new_match.teams.append(new_match_team)

#         # for team_member in team.members, loop 5x
#         # match_team_input.players and team.members MUST BE SORTED
#         for index, player_input in enumerate(match_team_input.players):
#             # for each player on the team

#             # set is_captain helper bool
#             is_captain = match_team_input.captain_id == player_input.player_id
#             # update TeamPlayer aggregate stats
#             team_player = team.members[index]
#             aggregates.update_player_aggregates(team_player, player_input, is_captain)

#             # update Player aggregate stats
#             player = team_player.player
#             aggregates.update_player_aggregates(player, player_input, is_captain)
#             aggregates.update_team_aggregates(player, match_team_input, rounds_lost)

#             # create MatchPlayer
#             new_match_player = MatchPlayer(
#                 player_id=player_input.player_id,
#                 kills=player_input.kills,
#                 assists=player_input.assists,
#                 deaths=player_input.deaths,
#                 mvps=player_input.mvps,
#                 score=player_input.score,
#                 adr=player_input.adr,
#                 steam_username=team_player.player.steam_username,
#                 steam_avatar_hash=team_player.player.steam_avatar_hash,
#             )
#             new_match_team.players.append(new_match_player)

#             # set rounds_lost for team2
#             rounds_lost = match_input.team1.rounds_won

#     db.session.add(new_match)
#     db.session.commit()
