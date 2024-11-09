from sqlalchemy import inspect

from apps import db

class Model(db.Model):
    __tablename__ = 'model'

    id = db.Column(db.Integer(), primary_key=True)
    model_name = db.Column(db.String())
    make_id = db.Column(db.Integer(), db.ForeignKey('make.id'))

    make = db.relationship('Make', backref='model')


    def __init__(self, model_name, make_id):
        self.model_name = model_name
        self.make_id = make_id
