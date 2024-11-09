from sqlalchemy import inspect

from apps import db

class Car(db.Model):
    __tablename__ = 'car'

    id = db.Column(db.Integer(), primary_key=True)
    model_id = db.Column(db.Integer(), db.ForeignKey('model.id'))
    make_id = db.Column(db.Integer(), db.ForeignKey('make.id'))
    image = db.Column(db.String())
    description = db.Column(db.String())

    make = db.relationship('Make', backref='car')
    model = db.relationship('Model', backref='car')

    def __init__(self, model_id, make_id, description, image = None):
        self.model_id = model_id
        self.make_id = make_id
        self.description = description
        if image:
            self.image = image
