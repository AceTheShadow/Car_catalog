from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired
from apps.make.models import Make


class CreateModelForm(FlaskForm):

    name = StringField('Model name',
                         id='model_name',
                         validators=[DataRequired()])
    make = SelectField('Choose make',
                          id='choose_make',
                          validators=[DataRequired()],
                          coerce=int)

    def __init__(self, *args, **kwargs):
        super(CreateModelForm, self).__init__(*args, **kwargs)
        self.make.choices = [(item.id, item.make_name)
                                        for item in Make.query.all()]

