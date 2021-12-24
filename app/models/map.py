
from app import db 

class Map(db.Model): # map info

    id: int = db.Column(db.Integer, primary_key=True)
    filename: str = db.Column(db.String(32), unique=True, nullable=False) # ex. de_dust2, de_cbble, pk
    map_name: str = db.Column(db.String(32), unique=True, nullable=False) # ex. Dust II, Cobblestone
    is_active_duty: bool = db.Column(db.Boolean(), nullable=False) # is the map in the competitive map pool?
    # anything else? image column ?

    matches = db.relationship('Match', back_populates='map', lazy='dynamic') # a Map is played in many Matches   

    def __repr__(self):
        return f'{self.__class__.__name__}<id: {self.id}, filename: {self.filename}, name: {self.map_name}, active_duty: {self.is_active_duty}>'
