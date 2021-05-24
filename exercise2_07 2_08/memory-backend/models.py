from app import db

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String())    

    def __init__(self, todo):
        self.todo = todo

    def __repr__(self):
        return '<id {}>'.format(self.id)