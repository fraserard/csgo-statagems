from ..extensions import db

class Admin(db.Model): # map info
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False) # player id of admin
    clearance = db.Column(db.SmallInteger, nullable=False) # clearance level admin. 0 = all perms 

    def __repr__(self):
        return f'{self.__class__.__name__}<id: {self.id}, clearance: {self.clearance}>'