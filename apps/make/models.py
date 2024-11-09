from sqlalchemy import inspect

from apps import db

class Make(db.Model):
    __tablename__ = 'make'

    id = db.Column(db.Integer(), primary_key=True)
    make_name = db.Column(db.String())
    country_id = db.Column(db.Integer(), db.ForeignKey('country.id'))

    country = db.relationship('Country', backref='makes')

    def __init__(self, make_name, country_id):
        self.make_name = make_name
        self.country_id = country_id
