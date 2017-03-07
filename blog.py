# jinja is the template manager, and webapp the Google Framework
# are working on
import jinja2
import os
import webapp2

# from google.appengine.ext import db

# My modules
import database
import hashing

# get the machine direction where jinja takes the templates from
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# Sets up jinja configuration.
# The autoescape is to avoid sneaky HTML tags or malicious scripts on forms
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)


class Handler(webapp2.RequestHandler):
    """ Instance of the Google App Engine framework """
    def get(self):
        self.redirect('/blog/?')

    def write(self, *a, **params):
        # Writes whatever you pass as param
        self.response.out.write(*a, **params)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **params):
        # Renders the template, with optional parameters
        self.write(self.render_str(template, **params))

    def set_cookie(self, uid):
        # Creates a hashed cookie value
        cookie = hashing.make_secure_val(str(uid))
        # Add cookie to header
        self.response.headers.add_header('Set-Cookie',
        'userid=%s; Path=/' % cookie)

    def check_cookie(self, cookie):
        # Checks if cookie is correct
        uid = cookie.split('|')[0]
        if hashing.check_secure_val(cookie) == uid:
            # User method to return instance with id
            return database.User.by_id(int(uid))

    def get_user_cookie(self):
        # Gets a cookie and checks if correct
        uid_cookie = self.request.cookies.get('userid')
        return self.check_cookie(uid_cookie)

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        # Gets cookie
        uid_cookie = self.request.cookies.get('userid')
        if uid_cookie:
            # logged_user is an instance of User db
            logged_user = self.check_cookie(uid_cookie)
            # Creates a global variable to use in templates
            jinja_env.globals['username'] = logged_user.username
        else:
            jinja_env.globals['username'] = ''

# Modules are set here, because if declared on top it trows a
# circular dependent imports error (documented at Stack Overflow)
from index          import Index
from new            import New
from post           import Post
from signup         import Signup
from login          import Login
from logout         import Logout
from welcome        import Welcome
from edit           import Edit
from delete         import Delete
from like           import Like
from comment        import Comment
from delete_comment import Delete_comment
from edit_comment   import Edit_comment

# Routes
app = webapp2.WSGIApplication([('/?', Handler),
                               ('/blog/?', Index),
                               ('/blog/newpost', New),
                               ('/blog/(\d+)', Post),
                               ('/blog/signup', Signup),
                               ('/blog/login', Login),
                               ('/blog/logout', Logout),
                               ('/blog/welcome', Welcome),
                               ('/blog/edit', Edit),
                               ('/blog/delete', Delete),
                               ('/blog/like', Like),
                               ('/blog/comment', Comment),
                               ('/blog/delete_comment', Delete_comment),
                               ('/blog/edit_comment', Edit_comment)
                              ], debug=True)
