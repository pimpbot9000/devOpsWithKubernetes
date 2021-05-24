from app import db
from sqlalchemy.dialects.postgresql import JSON


class Ping(db.Model):
    __tablename__ = 'pings'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String())
    

    def __init__(self, timestamp):
        self.timestamp = timestamp

    def __repr__(self):
        return '<id {}>'.format(self.id)