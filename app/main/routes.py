from flask import Blueprint, render_template, redirect,url_for
from flask_login import current_user
#from app.models import  Quote

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    # if current_user.is_authenticated:
    #     #username=current_user.username
    #     return redirect((url_for('users.user_home', username=current_user.username)))
    # page = request.args.get('page', 1, type=int)
    # user = User.query.filter_by(username=username).first_or_404()
    # quotes = Quote.query.filter_by(author=user).paginate(page=page, per_page=2)
    return render_template('home.html')


@main.route('/about')
def about():
    return render_template('about.html', title='About')
