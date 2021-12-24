import os
import click
import requests
from flask import current_app
from sqlalchemy.orm import load_only
from app import db
from app.models import (
    Player, 
    Map, 
    Group, GroupPlayer, 
    Team, TeamPlayer, 
    Match, MatchPlayer, MatchTeam)

def register(app):
    
    @app.cli.group()
    def populate(): # flask populate
        """Statagems database population commands"""
        pass
    
    @populate.command()
    def all(): # flask populate all
        """Executes all database population commands"""        
        db.drop_all()
        db.create_all()
        
        populate_player()
        populate_map()
        populate_group()
        populate_team()
        db.session.commit()
        
    @populate.command()
    def player(): # flask populate player
        """Populates Player table"""
        populate_player()
        db.session.commit()
        
    @populate.command()
    def map(): # flask populate map
        """Populates Map table"""
        populate_map()
        db.session.commit()
        
    @populate.command()
    def group(): # flask populate group
        """Populates Group, GroupPlayer table"""
        populate_group()
        db.session.commit()
        
        
    @populate.command()
    def team(): # flask populate team
        """Populates Team, TeamPlayer table"""
        populate_team()
        db.session.commit()

def populate_team():
    team1 = Team(group_id=1)
    team1_members = [
        TeamPlayer(player_id=1),
        TeamPlayer(player_id=2),
        TeamPlayer(player_id=3),
        TeamPlayer(player_id=4),
        TeamPlayer(player_id=5)
    ]
    for member in team1_members: 
        team1.members.append(member)
    team2 = Team(group_id=1)
    team2_members = [
        TeamPlayer(player_id=6),
        TeamPlayer(player_id=7),
        TeamPlayer(player_id=8),
        TeamPlayer(player_id=9),
        TeamPlayer(player_id=10)
    ]
    for member in team2_members: 
        team2.members.append(member)
        
    db.session.add(team1)
    db.session.add(team2)
    db.session.flush()
    
def populate_group():
    group_name = 'Test Tenner Group'
    description = 'Test Tenner World Cup - \
        Nail biting matches between the TestYoungsters and the TestChildren!'
    
    group = Group(group_name=group_name, 
                  description=description)
    
    player = Player.query.filter_by(steam_id = current_app.config["ADMIN_STEAM_ID"]).first()
    group_player = GroupPlayer(player_id=player.id, 
                               group_username=player.steam_username,
                               group_clearance=0)
    
    group.members.append(group_player)
    
    db.session.add(group)
    db.session.flush()
    
    members = [
        GroupPlayer(group_id=1, player_id=2, group_username="Player Two"),
        GroupPlayer(group_id=1, player_id=3, group_username="Player Three"),
        GroupPlayer(group_id=1, player_id=4, group_username="Player Four"),
        GroupPlayer(group_id=1, player_id=5, group_username="Player Five"),
        GroupPlayer(group_id=1, player_id=6, group_username="Player Six"),
        GroupPlayer(group_id=1, player_id=7, group_username="Player Seven"),
        GroupPlayer(group_id=1, player_id=8, group_username="Player Eight"),
        GroupPlayer(group_id=1, player_id=9, group_username="Player Nine"),
        GroupPlayer(group_id=1, player_id=10, group_username="Player Ten")
    ]
    db.session.add_all(members)
    db.session.flush()

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
    
def populate_player():
    STEAM_API_KEY = current_app.config["STEAM_API_KEY"]
    ADMIN_STEAM_ID = current_app.config["ADMIN_STEAM_ID"]
    
    resp = requests.get(f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={STEAM_API_KEY}&steamids={ADMIN_STEAM_ID}')
    admin_data = resp.json()
    admin_data = admin_data['response']['players'][0]
    faffers = Player(
        steam_id = admin_data['steamid'],
        steam_username = admin_data['personaname'][:32],
        steam_avatar_hash = admin_data['avatarhash'],
        is_admin = True
    )
    if 'realname' in admin_data:
                faffers.steam_real_name = (admin_data['realname'])[:64]
    db.session.add(faffers)

    resp = requests.get(f'https://api.steampowered.com/ISteamUser/GetFriendList/v1/?key={STEAM_API_KEY}&steamid={ADMIN_STEAM_ID}')
    friends_list = resp.json()
    friends_list = friends_list['friendslist']['friends']
    steamid_list = []
    for f in friends_list:
        steamid_list.append(f['steamid'])

    resp = requests.get(f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={STEAM_API_KEY}&steamids={steamid_list}')
    players_data = resp.json()
    players_data = players_data['response']['players']

    for p in players_data:
        player = Player.query.options(load_only('steam_id', 'steam_username', 'steam_real_name', 'steam_avatar_hash')).filter_by(steam_id=p['steamid']).first()
        if player is None: # if new registration, make new player from steam api data
            new_player = Player(
            steam_id = p['steamid'],
            steam_username = p['personaname'][:32], 
            steam_avatar_hash = p['avatarhash'] )
            if 'realname' in p:
                new_player.steam_real_name = (p['realname'])[:64]
        
            db.session.add(new_player)
        else: # if player exists, update from steam api data
            if player.steam_username != p['personaname']:
                player.steam_username = p['personaname'][:32]
            if 'realname' in p:
                if player.steam_real_name != p['realname']:
                    player.steam_real_name = (p['realname'])[:64]
            if player.steam_avatar_hash != p['avatarhash']:
                player.steam_avatar_hash = p['avatarhash']
            
    db.session.flush()