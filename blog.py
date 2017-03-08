# Webapp written in Python, using Google App Engine, that allows you publish
# your own posts and like someone elses!

import webapp2

# My modules
from python_blog.controllers.handler import Handler  # Main handler
from python_blog.controllers.index import RHIndex
from python_blog.controllers.new import RHNew
from python_blog.controllers.post import RHPost
from python_blog.controllers.signup import RHSignup
from python_blog.controllers.login import RHLogin
from python_blog.controllers.logout import RHLogout
from python_blog.controllers.welcome import RHWelcome
from python_blog.controllers.edit import RHEdit
from python_blog.controllers.delete import RHDelete
from python_blog.controllers.like import RHLike
from python_blog.controllers.comment import RHComment
from python_blog.controllers.delete_comment import RHDeleteComment
from python_blog.controllers.edit_comment import RHEditComment

# Routes
app = webapp2.WSGIApplication([('/?', Handler),
                               ('/blog/?', RHIndex),
                               ('/blog/newpost', RHNew),
                               ('/blog/(\d+)', RHPost),
                               ('/blog/signup', RHSignup),
                               ('/blog/login', RHLogin),
                               ('/blog/logout', RHLogout),
                               ('/blog/welcome', RHWelcome),
                               ('/blog/edit', RHEdit),
                               ('/blog/delete', RHDelete),
                               ('/blog/like', RHLike),
                               ('/blog/comment', RHComment),
                               ('/blog/delete_comment', RHDeleteComment),
                               ('/blog/edit_comment', RHEditComment)
                               ], debug=True)
