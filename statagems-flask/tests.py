from datetime import datetime

import unittest

from config import Config
from app import create_app, db
from app.models import (
    Map, Match, MatchTeam, MatchPlayer, Team, TeamPlayer
)


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:admin@localhost:3306/statagems_test'

class MapModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_map(self):
        inferno = Map(filename='de_inferno', map_name='Inferno', is_active_duty=True)
        train = Map(filename='de_train', map_name='Train', is_active_duty=False)
        db.session.add(inferno)
        db.session.add(train)
        db.session.commit()
        
        inferno = Map.query.filter_by(filename='de_inferno').first()
        self.assertEqual(inferno.is_active_duty, True)
        
        train = Map.query.filter_by(map_name='Train').first()
        self.assertEqual(train.is_active_duty, False)
        
    def test_add_finished_match(self):
        # first entry from 10 man stats excel 
        match_data = {
            'map_id': 1, # Inferno
            'group_id': 1, # Tenner World
            'date_played': datetime.utcnow(),
            'teams': [
                {
                    'start_side': 'CT',
                    'captain_id': 3, # eddy
                    'rounds_won': 16,
                    'players': [
                        {
                            'group_player_id': 3, # eddy
                            'kills': 27,
                            'assists': 5,
                            'deaths': 14,
                            'mvps': 6,
                            'score': 66
                        },
                        {
                            'group_player_id': 18, # nayan
                            'kills': 22,
                            'assists': 4,
                            'deaths': 16,
                            'mvps': 3,
                            'score': 56
                        },
                        {
                            'group_player_id': 13, # aidan
                            'kills': 10,
                            'assists': 8,
                            'deaths': 20,
                            'mvps': 2,
                            'score': 33
                        },
                        {
                            'group_player_id': 17, # liam
                            'kills': 19,
                            'assists': 6,
                            'deaths': 19,
                            'mvps': 1,
                            'score': 52
                        },
                        {
                            'group_player_id': 5, # ak
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
                            'group_player_id': 22, # joel
                            'kills': 24,
                            'assists': 4,
                            'deaths': 22,
                            'mvps': 2,
                            'score': 58,
                        },
                        {
                            'group_player_id': 4, # josh
                            'kills': 20,
                            'assists': 0,
                            'deaths': 19,
                            'mvps': 3,
                            'score': 49
                        },
                        {
                            'group_player_id': 8, # jack
                            'kills': 13,
                            'assists': 2,
                            'deaths': 24,
                            'mvps': 2,
                            'score': 32
                        },
                        {
                            'group_player_id': 2, # will
                            'kills': 18,
                            'assists': 3,
                            'deaths': 20,
                            'mvps': 1,
                            'score': 46
                        },
                        {
                            'group_player_id': 10, # mark
                            'kills': 8,
                            'assists': 3,
                            'deaths': 21,
                            'mvps': 2,
                            'score': 29
                        }] 
                }]
        }
        
        


       

if __name__ == '__main__':
    unittest.main(verbosity=2)