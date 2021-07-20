# from ..extensions import db

# class TokenBlocklist(db.Model): # table of revoked refresh tokens
#     __tablename__ = 'token_blocklist'

#     id = db.Column(db.Integer, primary_key=True)
#     jti = db.Column(db.String(36), nullable=False)

#     def add(self):
#             db.session.add(self)
#             db.session.commit()
    
#     @classmethod
#     def is_jti_blacklisted(cls, jti):
#         query = cls.query.filter_by(jti = jti).first()
#         return bool(query)