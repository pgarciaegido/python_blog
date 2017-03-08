import os

# jinja is the template manager
import jinja2
import webapp2

# My modules
from python_blog.models.user import User
import python_blog.utils.hashing as hashing

# get the machine direction where jinja takes the templates from
template_dir = os.path.join(os.path.dirname(__file__), '../../templates')
# Sets up jinja configuration.
# The autoescape is to avoid sneaky HTML tags or malicious scripts on forms
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class Handler(webapp2.RequestHandler):
    """ Instance of the Google App Engine framework """
    def get(self):
        self.redirect('/blog/?')

    def write(self, *a, **params):
        """ Writes whatever you pass as param """
        self.response.out.write(*a, **params)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **params):
        """ Renders the template, with optional parameters """
        self.write(self.render_str(template, **params))

    def set_cookie(self, uid):
        """ Creates a hashed cookie value """
        cookie = hashing.make_secure_val(str(uid))
        # Add cookie to header
        self.response.headers.add_header('Set-Cookie',
                                         'userid=%s; Path=/' % cookie)

    def check_cookie(self, cookie):
        """ Checks if cookie is correct """
        uid = cookie.split('|')[0]
        if hashing.check_secure_val(cookie) == uid:
            # User method to return instance with id
            return User.by_id(int(uid))

    def get_user_cookie(self):
        """ Gets a cookie and checks if correct """
        uid_cookie = self.request.cookies.get('userid')
        if uid_cookie is None:
            return None
        else:
            return self.check_cookie(uid_cookie)

    def initialize(self, *a, **kw):
        """ Checks if user is logged """
        webapp2.RequestHandler.initialize(self, *a, **kw)
        # Gets cookie
        uid_cookie = self.request.cookies.get('userid')
        if uid_cookie:
            # logged_user is an instance of User db
            logged_user = self.check_cookie(uid_cookie)
            # If cookie is not correct
            if logged_user is None:
                self.write('Denied')
            # Creates a global variable to use in templates
            else:
                jinja_env.globals['username'] = logged_user.username
        else:
            jinja_env.globals['username'] = ''
