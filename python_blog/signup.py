# from google.appengine.ext import db

# Built in modules
import re
import hashlib

# My modules
from blog import Handler
import database
import signup_validate as sv
import hashing
import config


class Signup(Handler):
    def get(self):
        self.render("signup.html")

    def post(self):
        # Get values from form inputs
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        valid = True

        # These functions come from signup_validate
        # Checks username
        if sv.valid_username(username) is None:
            valid = False
            user_warn = sv.error_messages['user_warn']

        else:
            user_warn = ''

        # If username doesn't exist
        if database.User.by_username(username) is None:
            user_warn = ''

        else:
            valid = False
            user_warn = sv.error_messages['user_exists']

        # If password is not valid
        if sv.valid_password(password) is None:
            valid = False
            pass_warn = sv.error_messages['pass_warn']
        else:
            pass_warn = ''

        # If validate and password are not equal
        if password != verify:
            valid = False
            verify_warn = sv.error_messages['verify_warn']
        else:
            verify_warn = ''

        # If email is valid
        if sv.valid_email(email) is None and email != '':
            valid = False
            email_warn = sv.error_messages['email_warn']
        else:
            email_warn = ''

        # If there is no mistake, redirect, taking the username
        if valid:
            # Hashes password
            p = hashing.make_pw_hash(username, password)
            # Creates a register in db
            u = database.User(username=username, password=p, email=email)
            u.put()

            # Gets id from entity
            uid = u.key().id()
            # Sets cookie
            self.set_cookie(uid)

            self.redirect('/blog/welcome')
        # If there is any mistake, renders form with prev values and warns
        else:
            self.render('signup.html', user_input=username,
                        user_warn=user_warn, pass_warn=pass_warn,
                        verify_warn=verify_warn, email_warn=email_warn,
                        email_input=email)
