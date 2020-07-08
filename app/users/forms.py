from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, SelectField
from wtforms.validators import Length, Email, EqualTo, InputRequired
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class UpdateAccountForm(FlaskForm):
    # username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    # email = StringField('Email', validators=[DataRequired(), Email()])
    choices = [(' ', ' '), ('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AS', 'American Samoa'),
               ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'),
               ('DC', 'District of Columbia'),
               ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'),
               ('IA', 'Iowa'),
               ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'),
               ('LA', 'Louisiana'),
               ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'),
               ('MO', 'Missouri'), ('MP', 'Northern Mariana Islands'), ('MS', 'Mississippi'), ('MT', 'Montana'),
               ('NA', 'National'),
               ('NC', 'NorthCarolina'), ('ND', 'NorthDakota'), ('NE', 'Nebraska'), ('NH', 'NewHampshire'),
               ('NJ', 'NewJersey'),
               ('NM', 'NewMexico'), ('NV', 'Nevada'), ('NY', 'NewYork'), ('OH', 'Ohio'), ('OK', 'Oklahoma'),
               ('OR', 'Oregon'),
               ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
               ('SD', 'SouthDakota'),
               ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'),
               ('VT', 'Vermont'),
               ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'WestVirginia'), ('WY', 'Wyoming')]
    full_name = StringField('Full Name', validators=[InputRequired(), Length(max=50)])

    def validate_full_name(self, full_name):
        p = str(full_name.data)
        print(p)

        if not all(x.isalpha() or x.isspace() for x in p):
            raise ValidationError('Please enter a valid name')
        if p.isspace():
            raise ValidationError('Please enter a valid name')

    address_one = StringField('Address 1', validators=[InputRequired(), Length(max=100)])
    address_two = StringField('Address 2', validators=[Length(max=100)])
    city = StringField('City', validators=[InputRequired(), Length(max=100)])
    state = SelectField('State', choices=choices, validators=[InputRequired()])
    zipcode = StringField('Zipcode', validators=[InputRequired()])

    def validate_zipcode(self, zipcode):
        print(zipcode.data)
        z = str(zipcode.data)
        print(zipcode.data)
        print(len(z))
        if not (len(z) == 9 or len(z) == 5):
            raise ValidationError('Zipcode should be either 5 or 9 digits')

    submit = SubmitField('Update')
