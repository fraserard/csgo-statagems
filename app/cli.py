from datetime import datetime
import logging
import os
import click

from flask import current_app
from app import db
from app.models import (
    Player, PlayerRoles,
    Map,)
from app.services import matches, players

def register(app):
    @app.cli.group()
    def statagems(): # flask statagems
        """Statagems commands"""
        pass
    
    # @statagems.command()
    # def match(): # flask statagems m
    #     # hog: Player = Player.query.get(1)
    #     # logging.error(list(hog.my_matches))
    #     matches = players.get_matches(1)

    #     logging.error(matches)
        
        
    @statagems.command()
    def init(): # flask statagems init
        """Initialize Statagems Instance"""
        
        # rebuild db
        db.drop_all()
        db.create_all()
        
        # seed db
        add_admin()
        whitelist_players()
        
        populate_map()
        
        db.session.commit()
    
    @app.cli.group()
    def populate(): # flask populate
        """Testing commands"""
        pass
    
    @populate.command()
    def match(): # flask populate match
        add_match()

def add_match():
    # first entry from 10 man stats excel 
    match_data = {
        'map_id': 1, # Inferno
        'teams': [
            {
                'start_side': 'CT',
                'captain_id': 3, # eddy
                'rounds_won': 16,
                'players': [
                    {
                        'player_id': 3, # eddy
                        'kills': 27,
                        'assists': 5,
                        'deaths': 14,
                        'mvps': 6,
                        'score': 66
                    },
                    {
                        'player_id': 18, # nayan
                        'kills': 22,
                        'assists': 4,
                        'deaths': 16,
                        'mvps': 3,
                        'score': 56
                    },
                    {
                        'player_id': 13, # aidan
                        'kills': 10,
                        'assists': 8,
                        'deaths': 20,
                        'mvps': 2,
                        'score': 33
                    },
                    {
                        'player_id': 17, # liam
                        'kills': 19,
                        'assists': 6,
                        'deaths': 19,
                        'mvps': 1,
                        'score': 52
                    },
                    {
                        'player_id': 5, # ak
                        'kills': 27,
                        'assists': 1,
                        'deaths': 15,
                        'mvps': 4,
                        'score': 58
                    }] 
            },
            {
                'start_side': 'T',
                'captain_id': 22, # joel
                'rounds_won': 10,
                'players': [
                    {
                        'player_id': 22, # joel
                        'kills': 24,
                        'assists': 4,
                        'deaths': 22,
                        'mvps': 2,
                        'score': 58,
                    },
                    {
                        'player_id': 4, # josh
                        'kills': 20,
                        'assists': 0,
                        'deaths': 19,
                        'mvps': 3,
                        'score': 49
                    },
                    {
                        'player_id': 8, # jack
                        'kills': 13,
                        'assists': 2,
                        'deaths': 24,
                        'mvps': 2,
                        'score': 32
                    },
                    {
                        'player_id': 2, # will
                        'kills': 18,
                        'assists': 3,
                        'deaths': 20,
                        'mvps': 1,
                        'score': 46
                    },
                    {
                        'player_id': 10, # mark
                        'kills': 8,
                        'assists': 3,
                        'deaths': 21,
                        'mvps': 2,
                        'score': 29
                    }] 
            }]
    }
    matches.add_match(match_data)
    

def populate_map():
    maps = [
        Map(filename='de_inferno',  map_name='Inferno',     is_active_duty=True),
        Map(filename='de_mirage',   map_name='Mirage',      is_active_duty=True),
        Map(filename='de_ancient',  map_name='Ancient',     is_active_duty=True),
        Map(filename='de_dust2',    map_name='Dust II',     is_active_duty=True),
        Map(filename='de_nuke',     map_name='Nuke',        is_active_duty=True),
        Map(filename='de_overpass', map_name='Overpass',    is_active_duty=True),
        Map(filename='de_vertigo',  map_name='Vertigo',     is_active_duty=True),
        Map(filename='de_cache',    map_name='Cache',       is_active_duty=False),
        Map(filename='de_train',    map_name='Train',       is_active_duty=False),
    ]
    db.session.add_all(maps)
    db.session.flush()
    
def add_admin():
    ADMIN_STEAM_ID = current_app.config["ADMIN_STEAM_ID"]
    
    admin = Player._players_from_steam(ADMIN_STEAM_ID)[0] # returns list, get 1st (and only) element
    
    admin.role = PlayerRoles.ADMIN
    
    db.session.add(admin)
    db.session.flush()
    
def whitelist_players():
    member_steam_ids = current_app.config["WHITELIST_STEAM_IDS"]

    Player.whitelist(member_steam_ids)
    
    db.session.flush()
