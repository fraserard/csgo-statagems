from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Gamer(db.Model):
    __tablename__ = 'gamer'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    rank = db.Column(db.String(50))

    def __repr__(self):
        return f"{self.username} ({self.rank})"

class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    steamId = db.Column(db.Integer, unique=True, nullable=True)