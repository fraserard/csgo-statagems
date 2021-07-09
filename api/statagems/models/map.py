from . import db

class Map(db.Model): # map info
    __tablename__ = 'map'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(32), unique=True) # ex. de_dust2, de_cbble, pk
    map_name = db.Column(db.String(32), unique=True) # ex. Dust II, Cobblestone
    # anything else? image column ?

    matches = db.relationship('Match', back_populates='map') # a Map is played in many Matches

    def __repr__(self):
        return f'{self.__class__.__name__}<file: {self.filename}, name: {self.map_name}>'