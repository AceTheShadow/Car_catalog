from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import TextAreaField, FileField
from wtforms.validators import DataRequired

from apps.make.models import Make
from apps.model.models import Model


class CreateCarForm(FlaskForm):

    make = SelectField('Choose make',
                          id='choose_make',
                          validators=[DataRequired()],
                          coerce=int)
    model = SelectField('Choose model',
                        id='choose_model',
                        validators=[DataRequired()],
                        coerce=int)
    description = TextAreaField('Description',
                                id='description')
    image = FileField('Select image',
                      id='image',
                      name='image')

    def __init__(self, *args, **kwargs):
        super(CreateCarForm, self).__init__(*args, **kwargs)
        self.make.choices = [(item.id, item.make_name)
                                        for item in Make.query.all()]
        self.model.choices = [(item.id, item.model_name)
                              for item in Model.query.all()]
