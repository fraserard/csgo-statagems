from datetime import datetime

from app import db

class Group(db.Model): # groups, users can join
 
    id: int = db.Column(db.Integer, primary_key=True) # group id
    
    group_name: str = db.Column(db.String(32), nullable=False) # name of group
    description: str = db.Column(db.String(255), nullable=True) # description of group

    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    matches = db.relationship('Match', back_populates='group') # a group can have many matches
    members = db.relationship('GroupPlayer', back_populates='group') # a group can have many members 
    teams = db.relationship('Team', back_populates='group') # a group can have many teams
    
    def __repr__(self):
        return f'{self.__class__.__name__}<Id: {self.id}, name: {self.group_name}>'

    