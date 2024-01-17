from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    HiddenField,
    RadioField,
    StringField,
    DecimalField,
    TextAreaField,
    SelectMultipleField,
)
from wtforms.validators import NumberRange, DataRequired, ValidationError, Optional


class SignButton(FlaskForm):
    sign = SubmitField("Sign Now")
