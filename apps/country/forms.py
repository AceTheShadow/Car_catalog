from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CreateCountryForm(FlaskForm):
    name = StringField('Country name',
                         id='country_name',
                         validators=[DataRequired()])
