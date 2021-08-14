from ..extensions import db

class FriendRequest(db.Model): # friend requests
    __tablename__ = 'friend_request'
 
    issuer_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True) # user who sent request
    recipient_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True) # user receiving request

    sent_at = db.Column(db.DateTime, server_default=db.func.now())

    issuing_user = db.relationship('Player', foreign_keys=issuer_id, back_populates='issued_requests') 
    receiving_user = db.relationship('Player', foreign_keys=recipient_id, back_populates='received_requests')
    
    def __repr__(self):
        return f'{self.__class__.__name__}<issuer_id: {self.issuer_id}, recipient_id: {self.recipient_id}>'