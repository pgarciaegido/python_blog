# My modules
from blog import Handler
from database import User
import hashing

class Welcome(Handler):
    def get(self):
        # Get userid cookie
        u = self.get_user_cookie()
        if u:
            self.write('welcome! your username is: %s ' % u.username)
        else:
            self.redirect('/blog/signup')
