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


class SignForm(FlaskForm):
    name = StringField(
        "What is your name?", validators=[DataRequired()], description="Enter name"
    )
    email = StringField(
        "What is your email address?",
        validators=[DataRequired()],
        description="Enter email",
    )

    promo_email = RadioField(
        label="Please check the box if you prefer NOT to receive occasional emails related to the Planner's Pledge.",
        choices=["<Do not send>"],
        validators=[Optional()],
    )
    profession = RadioField(
        label="What is your profession?",
        validators=[Optional()],
        choices=[
            "Architect",
            "Engineer",
            "Landscape Architect",
            "Planner",
            "Urban Designer",
        ],
    )
    profession_other = StringField(
        label="Other profession",
        validators=[Optional()],
        description="Enter other profession",
    )
    sign_name = StringField(
        label="Sign the Planner's Pledge by typing your full name in the box below.",
        validators=[DataRequired()],
        description="Sign the pledge with your name!",
    )

    certification = RadioField(
        label="What is your profession?",
        validators=[Optional()],
        choices=[
            "AICP (American Planning Association)",
            "CNU-A (Congress for the New Urbanism)",
            "Professional Transportation Planner (Institute of Transportation Engineers)",
        ],
    )
    certification_other = StringField(
        label="Other certification",
        validators=[Optional()],
        description="Enter other certification",
    )
    sector = RadioField(
        label="In which sector do you currently work?",
        validators=[Optional()],
        choices=[
            "Academic",
            "Non-profit",
            "Private",
            "Public",
        ],
    )
    sector_other = StringField(
        label="Other sector",
        validators=[Optional()],
        description="Enter other sector",
    )
    age = RadioField(
        label="What is your age",
        validators=[Optional()],
        choices=["18-24", "25-34", "35-44", "45-54", "55-64", "65 or older"],
    )
    gender = RadioField(
        label="What is your gender",
        validators=[Optional()],
        choices=[
            "Male",
            "Female",
            "Non-binary",
            "Prefer not to answer",
        ],
    )
    gender_other = StringField(
        label="Other gender",
        validators=[Optional()],
        description="Enter self-identified response",
    )
    race = RadioField(
        label="What is your race? [Check all that apply]",
        validators=[Optional()],
        choices=[
            "American Indian or Alaska Native",
            "Asian",
            "African American/Black",
            "Native Hawaiian or Pacific Islander",
            "Caucasian/White",
            "Prefer not to answer",
        ],
    )
    race_other = StringField(
        label="Other race",
        validators=[Optional()],
        description="Enter self-identified response",
    )
    ethn_hisp = RadioField(label="Are you Hispanic/Latino?", choices=["Yes", "No"])

    sign = SubmitField("Sign the Pledge")
