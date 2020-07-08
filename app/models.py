from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    quotes = db.relationship('Quote', backref='author', lazy=True)
    user_profile = db.relationship('UserProfile', backref='author', lazy=True, uselist=False)

    # user_profile_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gallons_requested = db.Column(db.Float(), nullable=False)
    date_requested = db.Column(db.Text(), nullable=False, default=datetime.utcnow)
    delivery_address = db.Column(db.String(120), nullable=False)
    suggested_price = db.Column(db.Float(), nullable=True)
    total_amount_due = db.Column(db.Float(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # user_profile_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)

    def __repr__(self):
        return f"Quote('{self.gallons_requested}', '{self.date_requested}')"


class UserProfile(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    address_one = db.Column(db.String(100), nullable=False)
    address_two = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zipcode = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"UserProfile('{self.full_name}')"
