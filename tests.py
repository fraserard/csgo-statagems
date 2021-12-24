import unittest

from app import create_app, db
from app.models import Map
from config import Config

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
        

if __name__ == '__main__':
    unittest.main(verbosity=2)