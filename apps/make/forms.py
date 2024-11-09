from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired

from apps.country.models import Country


class CreateMakeForm(FlaskForm):

    name = StringField('Make name',
                         id='make_name',
                         validators=[DataRequired()])
    country = SelectField('Choose country',
                          id='choose_country',
                          validators=[DataRequired()],
                          coerce=int)

    def __init__(self, *args, **kwargs):
        super(CreateMakeForm, self).__init__(*args, **kwargs)
        self.country.choices = [(item.id, item.name)
                                        for item in Country.query.all()]

