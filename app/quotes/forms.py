from flask_wtf import FlaskForm
# from flask_datepicker import flask_datepicker
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, IntegerField, DateField, \
    Label, FloatField, DecimalField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, NumberRange, Regexp, Optional
from app.models import User, UserProfile


# from flask_bootstrap import Bootstrap
# from flask_datepicker import flask_datepicker

# flask_datepicker(app)

class QuoteForm(FlaskForm):
    # def validate_gallons_requested(self, gallons_requested):
    #     print(gallons_requested.isdigit())
    #     if not gallons_requested.isdigit():
    #         raise ValidationError('Gallons requested should be a number')

    gallons_requested = FloatField('Gallons Requested',
                                   validators=[DataRequired()])
    delivery_address = StringField('Delivery Address', render_kw={'readonly': True})
    date_requested = DateField('Date Requested', format='%Y-%m-%d', validators=[DataRequired()])
    suggested_price = StringField('Suggested Price Per Gallon', render_kw={'readonly': True})
    total_amount_due = StringField('Total Amount Due', render_kw={'readonly': True})
    get_quote = SubmitField('Get Quote')
    get_price = SubmitField('Get Price')
