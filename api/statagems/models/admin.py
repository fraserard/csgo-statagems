from ..extensions import db
from .player import Player

class Admin(Player): # admin table, inherited from Player model
    # SINGLE TABLE INHERITANCE WITH PLAYER TABLE

    # clearance level of admin
    # 0 = delete (all priv), 1 = create, 2 = view only
    permission_clearance = db.Column(db.SmallInteger)

    __mapper_args__ = {
        'polymorphic_identity':'admin',
    }

    def __repr__(self):
        return f'{self.__class__.__name__}<id: {self.id}, clearance: {self.clearance}>'