from google.appengine.ext import db

import re
import hashlib
import logging

from blog import Handler
import database
import signup_validate as sv
import hashing

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
        if sv.valid_username(username) == None:
            valid = False
            user_warn = sv.error_messages['user_warn']
        else:
            user_warn = ''

        if database.User.by_username(username) == None:
            user_warn = ''
        else:
            valid = False
            user_warn = user_exists

        if sv.valid_password(password) == None:
            valid = False
            pass_warn = sv.error_messages['pass_warn']
        else:
            pass_warn = ''

        if password != verify:
            valid = False
        else:
            verify_warn = ''

        if sv.valid_email(email) == None and email != '':
            valid = False
            email_warn = sv.error_messages['email_warn']
        else:
            email_warn = ''

        # If there is no mistake, redirect, taking the username
        if valid:
            # Hashes password
            p = hashing.make_pw_hash(username, pw)
            logging.info(p)
            # Creates a register in db
            u = database.User(username=username, password=p, email=email)
            u.put()



            self.response.headers.add_header('Set-Cookie', 'username=%s; Path=/' % ck)
            self.redirect('/blog/welcome')
        # If there is any mistake, renders form with prev values and warns
        else:
            self.render('signup.html', user_input=username, user_warn=user_warn,
                         pass_warn=pass_warn, verify_warn=verify_warn,
                         email_warn=email_warn, email_input=email)
