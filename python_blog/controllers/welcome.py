# My modules
from handler import Handler
from python_blog.models.user import User


class RHWelcome(Handler):
    def get(self):
        # Get userid cookie
        u = self.get_user_cookie()
        if u:
            # self.write('welcome! your username is: %s. Redirecting...')
            self.render('welcome.html')

        else:
            self.redirect('/blog/signup')
