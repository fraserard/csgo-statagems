from ..extensions import db


class BlockList(db.Model): # user blocked list
    __tablename__ = 'block_list'
 
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True) # user who is issuing block
    blocked_player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True) # user who is getting blocked

    created_at = db.Column(db.DateTime, server_default=db.func.now())

    player = db.relationship('Player', foreign_keys=player_id, back_populates="issued_blocks")
    blocked_player = db.relationship('Player', foreign_keys=blocked_player_id, back_populates="received_blocks")

    def __repr__(self):
        return f'{self.__class__.__name__}<issuer_id: {self.issuer_id}, recipient_id: {self.recipient_id}>'

