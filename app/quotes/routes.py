from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify
from flask_login import current_user, login_required
from app import db
from app.models import Quote
from app.quotes.forms import QuoteForm

quotes = Blueprint('quotes', __name__)


@quotes.route("/quote/new", methods=['GET', 'POST'])
@login_required
def new_quote():
    if not current_user.user_profile:
        return redirect(url_for('users.account'))

    else:
        form = QuoteForm()
        # if form.validate_on_submit():
        # form.get_quote.disabled = True
        if request.method == 'GET':
            form.delivery_address.data = current_user.user_profile.address_one + ' ' + current_user.user_profile.address_two  # current_user.user_profile.address_one
            return render_template('create_quote.html', title='New Quote', form=form)
        print("***")
        print("###")
        if form.get_quote.data:
            print("$$$")
            quote = Quote(
                author=current_user,
                gallons_requested=form.gallons_requested.data,
                date_requested=form.date_requested.data,
                delivery_address=form.delivery_address.data,
                suggested_price=form.suggested_price.data,
                total_amount_due=form.total_amount_due.data,
            )
            db.session.add(quote)
            db.session.commit()
            flash('Your quote has been saved', 'success')
            return redirect(url_for('users.history'))
        elif form.get_price.data:
            # if form.validate_on_submit():
            print("@@@")
            if current_user.user_profile.state == 'TX':
                location_factor = 0.02
            else:
                location_factor = 0.04

            with db.session.no_autoflush:
                exists = db.session.query(db.exists().where(current_user.id == Quote.user_id)).scalar()

            if exists:
                rate_factor = 0.01
            else:
                rate_factor = 0
            # rate_factor=1

            if form.gallons_requested.data > 1000:
                gallons_requested_factor = 0.02
            else:
                gallons_requested_factor = 0.03

            date = str(request.form['date_requested'])

            year, month, datee = date.split("-")
            month = int(month)

            if month in range(3, 9):
                rate_fluctuation = 0.04
            else:
                rate_fluctuation = 0.03

            currentprice = 1.50
            company_profit_factor = 0.1

            margin = currentprice * (
                    location_factor - rate_factor + gallons_requested_factor + company_profit_factor +
                    rate_fluctuation)

            gallons = request.form['gallons_requested']
            suggestedprice = float(currentprice) + margin
            totalamt = float(gallons) * suggestedprice
            form.suggested_price.data = round(suggestedprice, 2)
            form.total_amount_due.data = round(totalamt, 2)
            form.get_quote.disabled = False

            return render_template('create_quote.html', title='New Quote', form=form)

    # return jsonify(data=form.errors)


@quotes.route("/quote/<int:quote_id>")
@login_required
def quote(quote_id):
    quote = Quote.query.get_or_404(quote_id)
    form = QuoteForm()
    form.gallons_requested.data = quote.gallons_requested
    # form.date_requested.data = quote.date_requested
    form.delivery_address.data = quote.delivery_address
    form.suggested_price.data = quote.suggested_price
    form.total_amount_due.data = quote.total_amount_due

    return render_template('quote.html', title=quote.date_requested, form=form)
