# dev_appserver.py .

# jinja is the template manager, and webapp the Google Framework
# are working on
import jinja2
import os
import webapp2
from google.appengine.ext import db

import hashing

# get the machine direction where jinja takes the templates from
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# Sets up jinja configuration.
# The autoescape is to avoid sneaky HTML tags or malicious scripts on forms
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)


class Handler(webapp2.RequestHandler):
    """ Instance of the framework """
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
        self.response.headers.add_header('Set-Cookie', 'userid=%s; Path=/' % cookie)


from index import Index
from new import New
from post import Post
from signup import Signup
from login import Login
from logout import Logout
from welcome import Welcome

# Routes
app = webapp2.WSGIApplication([('/blog/?', Index),
                               ('/blog/newpost', New),
                               ('/blog/(\d+)', Post),
                               ('/blog/signup', Signup),
                               ('/blog/login', Login),
                               ('/logout', Logout),
                               ('/blog/welcome', Welcome)
                              ], debug=True)
