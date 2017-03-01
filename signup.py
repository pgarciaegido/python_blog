from google.appengine.ext import db

import re
import hashlib
import logging

from blog import Handler
import database

class Signup(Handler):
    def get(self):
        self.render("signup.html")


    def post(self):
        # Get values from form inputs
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        # RE rules for validations
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        PASS_RE = re.compile(r"^.{3,20}$")
        EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

        # Error messages
        user_warn = 'The username is invalid'
        user_exists = 'The username already exists'
        pass_warn = 'The password is not valid'
        verify_warn = 'The passwords are not the same'
        email_warn = 'The email is not valid'

        # If it doesnt match, return None
        def valid_username(username):
            return USER_RE.match(username)

        def valid_password(password):
            return PASS_RE.match(password)

        def valid_email(email):
            return EMAIL_RE.match(email)

        valid = True

        if valid_username(username) == None:
            valid = False
        else:
            user_warn = ''

        if database.User.by_username(username) == None:
            user_warn = ''
        else:
            valid = False
            user_warn = user_exists

        if valid_password(password) == None:
            valid = False
        else:
            pass_warn = ''

        if password != verify:
            valid = False
        else:
            verify_warn = ''

        if valid_email(email) == None and email != '':
            valid = False
        else:
            email_warn = ''

        # If there is no mistake, redirect, taking the username
        if valid:
            u = database.User(username=username, password=password)
            u.put()
            # uid = str(random.randint(0,9999999))
            h = hashlib.sha256(username).hexdigest()
            ck = '%s|%s' % (str(username), h)
            self.response.headers.add_header('Set-Cookie', 'username=%s; Path=/' % ck)
            self.redirect('/blog/welcome')
        # If there is any mistake, renders form with prev values and warns
        else:
            self.render('signup.html', user_input=username, user_warn=user_warn,
                         pass_warn=pass_warn, verify_warn=verify_warn,
                         email_warn=email_warn, email_input=email)
