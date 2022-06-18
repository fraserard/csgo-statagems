from typing import Protocol

from app import models



class FieldUpdater():
    model: models.GroupAggregates
    
        


class GroupStatistics(Protocol):
    rounds_won: int
    rounds_lost: int
    start_side: models.TeamSides


def update_group_aggregates(
    team_or_player: models.GroupAggregates,
    match_data: GroupStatistics,
):
    """
    Updates game and round aggregates on Team or Player profiles when a new match is added.
    Works for fields unique to both Team and Player.

    Fields that get updated: rounds_won, rounds_lost, games_won, games_lost, started_ct_times, started_t_times

    @team_or_player: Team or Player entity to update
    @team_data: AddMatchTeamInput. Team stats from new match
    @rounds_lost
    """

    if match_data.rounds_won > match_data.rounds_lost:
        team_or_player.games_won += 1
    elif match_data.rounds_won < match_data.rounds_lost:
        team_or_player.games_lost += 1
    else:
        team_or_player.games_tied += 1

    team_or_player.rounds_won += match_data.rounds_won
    team_or_player.rounds_lost += match_data.rounds_lost

    if match_data.start_side == models.TeamSides.CT:
        team_or_player.times_started_ct += 1
    elif match_data.start_side == models.TeamSides.T:
        team_or_player.times_started_t += 1

class KADFields(Protocol):
    kills: int
    assists: int
    deaths: int
    
def update_kills_assists_deaths(
    player: models.IndividualAggregates,
    kad_data: KADFields,
    is_captain: bool,
):
    """
    Updates stat aggregates on Player profiles when a new match is added.
    Works for fields unique to both Player and TeamPlayer.

    Fields that get updated: kills, assists, deaths, score, mvps, adr, adr_count.

    @player: Player or TeamPlayer entity to update
    @player_data: player stats from new match
    """

    player.kills += kad_data.kills
    player.assists += kad_data.assists
    player.deaths += kad_data.deaths
    # player.score += match_data.score if match_data.score else 0
    # player.mvps += match_data.mvps if match_data.mvps else 0

    # if match_data.adr:
    #     player.adr_count += 1

    #     # if first adr record, set adr
    #     if player.adr is None:
    #         player.adr = match_data.adr

    #     else:  # if previous adr records, recalculate average
    #         player.adr = recalculate_adr(player.adr_count, player.adr, match_data.adr)

    #     # TODO ADD HISTORICAL ADR TABLE

    if is_captain:
        player.times_captain += 1


class CaptainFields(Protocol):
    is_captain: bool
    

def update_captain(player: models.IndividualAggregates, captain_data: CaptainFields):
    if captain_data.is_captain:
        player.times_captain += 1
    player.times_captain_possible += 1
    

class ADRField(Protocol):
    adr: int


def update_adr(
    player: models.IndividualAggregates,
    adr_data: ADRField,
):

    player.adr_count += 1

    # if first adr record, set adr
    if player.adr is None:
        player.adr = adr_data.adr

    else:  # if previous adr records, recalculate average
        player.adr = _recalculate_adr(player.adr_count, player.adr, adr_data.adr)


def _recalculate_adr(adr_count: int, current_adr: int, new_match_adr: int) -> int:
    """
    Recalculates overall ADR when a new ADR stat is added.

    @adr_count: running total of adr added
    @current_adr: current player adr stat
    @new_match_adr: adr of new match
    """

    new_adr = ((current_adr * (adr_count - 1)) + new_match_adr) / adr_count
    return int(new_adr)

