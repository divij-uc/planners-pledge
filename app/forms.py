from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    RadioField,
    StringField,
    SelectMultipleField,
    BooleanField,
    widgets,
)
from wtforms.validators import DataRequired, ValidationError, Optional, Email
from better_profanity import profanity

profanity.load_censor_words()

def profanity_check(form, field):
    if profanity.contains_profanity(field.data):
        raise ValidationError('Please enter a name without profanity!')


class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """

    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class SignForm(FlaskForm):
    name = StringField(
        "What is your name?",
        validators=[DataRequired(message="Please enter your name!")],
        description="Enter name",
    )
    email = StringField(
        "What is your email address?",
        validators=[DataRequired(message="Please enter your E-mail ID!"), Email("Please enter a valid E-mail ID!")],
        description="Enter email",
    )

    promo_email = BooleanField(
        label="Please check the box if you prefer NOT to receive occasional emails related to the Planner's Pledge.",
        validators=[Optional()],
    )
    profession = RadioField(
        label="What is your profession?",
        validators=[Optional()],
        choices=[
            "Elected Official",
            "Planner",
            "Urban Designer",
            "Engineer",
            "Architect",
            "Landscape Architect",
            "Real Estate Professional",
            "",
        ],
    )
    profession_other = StringField(
        label="Other profession",
        validators=[Optional()],
        description="Enter other profession",
    )
    sign_name = StringField(
        label="Sign the Planner's Pledge by typing your full name in the box below.",
        validators=[
            DataRequired(message="Please enter your full name to sign the pledge!"),
            profanity_check
        ],
        description="Sign the pledge with your name!",
    )

    certification = MultiCheckboxField(
        label="Do you have a professional certification? Check all that apply.",
        validators=[Optional()],
        choices=[
            "AICP (American Planning Association)",
            "CNU-A (Congress for the New Urbanism)",
            "AIA (American Institute of Architects)",
            "ASLA (American Society of Landscape Architects)",
            "Registered Architect",
            "Professional Transportation Planner (Institute of transportation Engineers)",
            "AMI, ALI, or AEI (American Association of State Highway and Transportation Officials)",
            "",
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
            "Public",
            "Non-profit",
            "Business",
            "Academic",
            "",
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
        choices=[
            "Under 18",
            "18-24",
            "25-34",
            "35-44",
            "45-54",
            "55-64",
            "65 or older",
        ],
    )
    gender = RadioField(
        label="What is your gender",
        validators=[Optional()],
        choices=[
            "Male",
            "Female",
            "Non-binary",
            "Prefer not to answer",
            "",
        ],
    )
    gender_other = StringField(
        label="Other gender",
        validators=[Optional()],
        description="Enter self-identified response",
    )
    race = MultiCheckboxField(
        label="What is your race? [Check all that apply]",
        validators=[Optional()],
        choices=[
            "American Indian or Alaska Native",
            "Asian",
            "African American/Black",
            "Native Hawaiian or Pacific Islander",
            "Caucasian/White",
            "Prefer not to answer",
            "",
        ],
    )
    race_other = StringField(
        label="Other race",
        validators=[Optional()],
        description="Enter self-identified response",
    )
    ethn_hisp = RadioField(
        label="Are you Hispanic/Latino?",
        validators=[Optional()],
        choices=["Yes", "No"],
    )

    sign = SubmitField("Sign the Pledge")
