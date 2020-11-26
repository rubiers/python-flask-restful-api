from .db import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=True)
    username = db.Column(db.String(255), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'age': self.age,
            'username': self.username
        }
