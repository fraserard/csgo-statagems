# type: ignore
import csv

import click
from flask import current_app

from app import db
from app.models import Map, Player, PlayerRoles
from app.services.matches import NewMatch, NewMatchPlayer, NewMatchTeam, process_match
from app.services.teams import create_team_hash


def register(app):
    @app.cli.group()
    def statagems():  # flask statagems
        """Statagems commands"""
        pass

    @statagems.command()
    def parse():
        parse_csv()

    @statagems.command()
    def init():  # flask statagems init
        """Initialize Statagems"""

        # rebuild db
        db.drop_all()
        db.create_all()

        # seed db
        add_admin()
        whitelist_players()

        populate_maps()

        db.session.commit()


def populate_maps():
    maps = [
        Map(filename="de_inferno", map_name="Inferno", is_active_duty=True),
        Map(filename="de_mirage", map_name="Mirage", is_active_duty=True),
        Map(filename="de_ancient", map_name="Ancient", is_active_duty=True),
        Map(filename="de_dust2", map_name="Dust II", is_active_duty=True),
        Map(filename="de_nuke", map_name="Nuke", is_active_duty=True),
        Map(filename="de_overpass", map_name="Overpass", is_active_duty=True),
        Map(filename="de_vertigo", map_name="Vertigo", is_active_duty=True),
        Map(filename="de_cache", map_name="Cache", is_active_duty=False),
        Map(filename="de_train", map_name="Train", is_active_duty=False),
    ]
    db.session.add_all(maps)
    db.session.flush()


def add_admin():
    ADMIN_STEAM_ID = current_app.config["ADMIN_STEAM_ID"]

    admin = Player._players_from_steam(ADMIN_STEAM_ID)[
        0
    ]  # returns list, get 1st (and only) element
    admin.username = admin.steam_username
    admin.role = PlayerRoles.ADMIN

    db.session.add(admin)
    db.session.flush()


def whitelist_players():
    member_steam_ids = current_app.config["WHITELIST_STEAM_IDS"]

    Player.whitelist(member_steam_ids)

    db.session.flush()


def parse_csv():
    players_dict = {
        76561198062177171: "faff",
        76561198176197151: "punsy",
        76561197988109633: "kber",
        76561198838959373: "stove",
        76561198158829689: "ak",
        76561198068095040: "jirv",
        76561198352827609: "fridge",
        76561199047500771: "flungal",
        76561198106190641: "lonnie",
        76561199050002891: "wubby",
        76561198037295599: "balba",
        76561198162262332: "jethro",
        76561198297429584: "coop",
        76561198066462442: "mah",
        76561198133242942: "jam",
        76561198214989569: "gronz",
        76561198051758083: "hog",
        76561198041061244: "smunk",
        76561198418887453: "unit",
        76561198137967417: "ramy",
        76561198168390081: "joel",
        76561198079000147: "scott",
        76561198217635600: "energy",
        76561198021143797: "reggy",
        76561198067374430: "choppa",
        76561199059397737: "jremps",
        76561198185097210: "shimmy",
    }

    section = "match"  # match, team1, team2, player1, player2
    matches: list[NewMatch] = []
    match: NewMatch
    team1: NewMatchTeam
    team2: NewMatchTeam

    with open("10man.csv", newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            if len(row) == 0:
                team1.rounds_lost = team2.rounds_won
                team2.rounds_lost = team1.rounds_won
                team1_player_ids = {player.player_id for player in team1.players}
                team2_player_ids = {player.player_id for player in team2.players}
                team1.team_hash = create_team_hash(team1_player_ids)
                team2.team_hash = create_team_hash(team2_player_ids)

                match.team1 = team1
                match.team2 = team2
                matches.append(match)
                section = "match"
                continue

            if section == "match":
                map = db.session.query(Map).filter_by(map_name=row[0]).first()
                match: NewMatch = NewMatch(
                    map_id=map.id, date_played=row[1], team1=None, team2=None
                )
                section = "team1"
                continue

            if section == "team1":
                team1: NewMatchTeam = NewMatchTeam(
                    start_side=row[0],
                    rounds_won=int(row[1]),
                    rounds_lost=None,
                    players=[],
                    captain_id=None,
                    team_hash=None,
                )
                section = "player1"
                continue

            if section == "player1":
                steam_id = list(players_dict.keys())[
                    list(players_dict.values()).index(row[0])
                ]
                player_db = (
                    db.session.query(Player).filter_by(steam_id=steam_id).first()
                )
                player: NewMatchPlayer = NewMatchPlayer(
                    player_id=player_db.id,
                    kills=int(row[1]),
                    assists=int(row[2]),
                    deaths=int(row[3]),
                )
                team1.players.append(player)

                if len(team1.players) == 5:
                    section = "team2"
                continue

            if section == "team2":
                team2: NewMatchTeam = NewMatchTeam(
                    start_side=row[0],
                    rounds_won=int(row[1]),
                    rounds_lost=None,
                    players=[],
                    captain_id=None,
                    team_hash=None,
                )
                section = "player2"
                continue

            if section == "player2":
                steam_id = list(players_dict.keys())[
                    list(players_dict.values()).index(row[0])
                ]
                player_db = (
                    db.session.query(Player).filter_by(steam_id=steam_id).first()
                )
                player: NewMatchPlayer = NewMatchPlayer(
                    player_id=player_db.id,
                    kills=int(row[1]),
                    assists=int(row[2]),
                    deaths=int(row[3]),
                )
                team2.players.append(player)

                if len(team2.players) == 5:
                    section = "team2"
                continue

        csv_file.close

    for match in matches:
        match = process_match(match)
        db.session.commit()
