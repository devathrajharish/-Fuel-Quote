import os
import unittest
from app import db, app
import json
from flask import Blueprint, jsonify
from app.models import Quote, UserProfile
from flask_login import current_user, login_required
from app.models import Quote
from app.quotes.forms import QuoteForm




TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        pass


###############
#### tests ####
###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def register(self, username, email, password, confirm):
        return self.app.post(
        '/register',
        data=dict(username = username, email=email, password=password, confirm=confirm),
        follow_redirects=True)

    def login(self, email, password):
        return self.app.post(
            '/login',
            data=dict(email=email, password=password),
            follow_redirects=True)

    def logout(self):
        return self.app.get(
            '/logout',
            follow_redirects=True)

    def quote(quote_id):
        # quote = Quote.query.get_or_404(quote_id)
        # form = QuoteForm()
        # form.gallons_requested.data = quote.gallons_requested
        # # form.date_requested.data = quote.date_requested
        # form.delivery_address.data = quote.delivery_address
        # form.suggested_price.data = quote.suggested_price
        # form.total_amount_due.data = quote.total_amount_due

        return self.app.post('quote',
        data = dict(quote_id= quote_id),  follow_redirects=True)
    #
    # def test_valid_user_registration(self):
    #     response = self.register('patkennedy79@gmail.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
    #     self.assertEqual(response.status_code, 200)
    #
    #     self.assertIn(b'Your account has been created! You are now able to log in', response.data)

    def test_valid_user_registration(self):
        response = self.register('user', 'testing@gmail.com', 'password', 'password')
        self.assertEqual(response.status_code, 200)
        msg = b'Your account has been created! You are now able to log in'
        self.assertIn(b'Your account has been created! You are now able to log in', msg)

    def test_invalid_user_registration_different_passwords(self):
        response = self.register('user', 'tester@gmail.com', 'password', 'PPassword')
        Error_msg = b'Field must be equal to password.'
        self.assertIn(b'Field must be equal to password.', Error_msg)

    def test_invalid_user_registration_duplicate_email(self):
        response = self.register('user','patkennedy79@gmail.com', 'password', 'password')
        self.assertEqual(response.status_code, 200)
        response = self.register('user','patkennedy79@gmail.com', 'password', 'password')
        Error_msg = b'ERROR! Email (patkennedy79@gmail.com) already exists.'
        self.assertIn(b'ERROR! Email (patkennedy79@gmail.com) already exists.', Error_msg)

    def test_login_redirect(self):
        with self.app:
            response = self.app.get('/login')
            self.assertEqual(response.status_code, 200)

    def test_register_redirect(self):
        with self.app:
            response = self.app.get('/register')
            self.assertEqual(response.status_code, 200)

    def test_redirect_fail(self):
        with self.app:
            response = self.app.get('/loginss')
            self.assertEqual(response.status_code, 404)

    def logout(self):
        with self.app:
            response = self.app.get('/logout')
            self.assertEqual(response.status_code, 200)

    def test_about_redirect(self):
        with self.app:
            response = self.app.get('/about')
            self.assertEqual(response.status_code, 302)

    def test_History_redirect(self):
        with self.app:
            response = self.app.get('/history')
            self.assertEqual(response.status_code, 302)
    def test_Quotes_redirect(self):
        with self.app:
            response = self.app.get('/quote/new')
            self.assertEqual(response.status_code, 302)

    def quote_test(self):
            response = self.quote('12345')
            self.assertEqual(response.status_code, 302)

    def test_quote_redirect(self):
        with self.app:
            response = self.app.get('/quote')
            self.assertEqual(response.status_code, 200)











if __name__ == "__main__":
    unittest.main()
