from blog import Handler
import hashing
from database import User
import logging

class Welcome(Handler):
    def get(self):
        # Get userid cookie
        uid_cookie = self.request.cookies.get('userid')

        if not uid_cookie:
            self.redirect('/blog/signup')

        uid = uid_cookie.split('|')[0]
        if hashing.check_secure_val(uid_cookie) == uid:
            # User method to return object with id
            u = User.by_id(int(uid))
            self.write('welcome! your username is: %s ' % u.username)
