# My modules
from blog import Handler
import database
import hashing
import logging

class Login(Handler):
    def get(self):
        self.render('login.html')

    def post(self):
        user = self.request.get('username')
        password = self.request.get('password')

        # Get user from db using username
        user_db = database.User.by_username(user)
        logging.info(user_db)
        # If user does not exist
        if user_db == None:
            error = "This user does not exist"
            # Render with error message
            self.render('login.html', error=error, user=user)

        else:
            # Check if hased password registered in db match with pass input
            # If correct
            if(hashing.valid_pw(user, password, user_db.password)):
                # Gets id from entity
                logging.info('pasa???')
                uid = user_db.key().id()
                # Sets cookie
                self.set_cookie(uid)
                self.redirect('/blog/welcome')

            # If incorrect render with error message
            else:
                error = "The password is not correct"
                self.render('login.html', error=error, user=user)
