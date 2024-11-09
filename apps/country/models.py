from sqlalchemy import inspect

from apps import db

class Country(db.Model):
    __tablename__ = 'country'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name
