from ..extensions import db


class Friend(db.Model): # friend relationships
    __tablename__ = 'friend'
 
    player1_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True) # user who sent request, issuer
    player2_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True) # user who received request, recipient

    friends_since = db.Column(db.DateTime, server_default=db.func.now())

    player_issuer = db.relationship('Player', foreign_keys=[player1_id], back_populates="issued_friends")
    player_recipient = db.relationship('Player', foreign_keys=[player2_id], back_populates="received_friends")

    def __repr__(self):
        return f'{self.__class__.__name__}<issuer_id: {self.player1_id}, recipient_id: {self.player2_id}>'



