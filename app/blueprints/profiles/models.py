from app import db


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    avatar = db.Column(db.Text, unique=True, nullable=True)  # fixme
    age = db.Column(db.Integer, nullable=True)
    city = db.Column(db.String(100), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
