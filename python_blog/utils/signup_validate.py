import re

# RE rules for validations
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

# Error messages
error_messages = {
    "user_warn": 'The username is invalid',
    "user_exists": 'The username already exists',
    "pass_warn": 'The password is not valid',
    "verify_warn": 'The passwords are not the same',
    "email_warn": 'The email is not valid'
}


# If it doesnt match, return None
def valid_username(username):
    return USER_RE.match(username)


def valid_password(password):
    return PASS_RE.match(password)


def valid_email(email):
    return EMAIL_RE.match(email)
