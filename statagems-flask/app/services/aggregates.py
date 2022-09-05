from typing import TYPE_CHECKING

from app import models

if TYPE_CHECKING:
    from app.services.matches import NewMatchPlayer, NewMatchTeam


def update_times_captain(model: models.IndividualAggregates, is_captain: bool) -> None:
    if is_captain:
        model.times_captain += 1
    model.times_captain_possible += 1


def update_individual_aggregates(
    model: models.IndividualAggregates,
    match_data: "NewMatchPlayer",
) -> None:

    model.kills += match_data.kills
    model.assists += match_data.assists
    model.deaths += match_data.deaths


def update_group_aggregates(
    model: models.GroupAggregates,
    match_data: "NewMatchTeam",
) -> None:
    """
    Updates game and round aggregates on Team or Player profiles when a new match is added.
    Works for fields unique to both Team and Player.

    Fields that get updated: rounds_won, rounds_lost, games_won, games_lost, started_ct_times, started_t_times

    @team_or_player: Team or Player entity to update
    @team_data: AddMatchTeamInput. Team stats from new match
    @rounds_lost
    """

    if match_data.rounds_won > match_data.rounds_lost:
        model.games_won += 1
    elif match_data.rounds_won < match_data.rounds_lost:
        model.games_lost += 1
    else:
        model.games_tied += 1

    model.rounds_won += match_data.rounds_won
    model.rounds_lost += match_data.rounds_lost

    if match_data.start_side == models.TeamSides.CT.value:
        model.times_started_ct += 1
    elif match_data.start_side == models.TeamSides.T.value:
        model.times_started_t += 1


def update_adr(
    player: models.IndividualAggregates,
    adr: int,
):

    player.adr_count += 1

    # if first adr record, set adr
    if player.adr is None:
        player.adr = adr

    else:  # if previous adr records, recalculate average
        player.adr = _recalculate_adr(player.adr_count, player.adr, adr)


def _recalculate_adr(adr_count: int, current_adr: int, new_match_adr: int) -> int:
    return int(((current_adr * (adr_count - 1)) + new_match_adr) / adr_count)
