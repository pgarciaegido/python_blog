# My modules
from blog     import Handler
from database import User
import hashing

import time

class Welcome(Handler):
    def get(self):
        # Get userid cookie
        u = self.get_user_cookie()
        if u:
            # self.write('welcome! your username is: %s. Redirecting...')
            self.render('welcome.html')

        else:
            self.redirect('/blog/signup')
