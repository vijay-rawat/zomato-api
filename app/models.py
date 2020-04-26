from app import db


class User(db.Model):
    # __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    phone = db.Column(db.String(50))
    address = db.Column(db.String(100))
    dob = db.Column(db.Date())

    def __repr__(self):
        return '<User {}>'.format(self.username)
