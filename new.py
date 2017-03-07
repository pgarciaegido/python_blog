# My modules
from blog import Handler
import database

class New(Handler):
    def render_front(self, subject="", content="", author="", error=""):
        # Selects newpost template, with default empty strings for form inpts
        self.render("newpost.html", subject=subject, content=content,
                                    author=author, error=error)

    def get(self):
        # Check cookies to see if user is logged
        if self.request.cookies.get('userid') == '':
            self.redirect('/blog/signup')
        else:
            self.render_front()

    def post(self):
        # Get both the subject and the content
        subject = self.request.get('subject')
        content = self.request.get('content')
        author  = self.get_user_cookie().username
        likes   = 0

        if subject and content:
            # If both exist, create new db instance
            e = database.Entry(subject = subject, content = content, author = author, likes=likes)
            # This saves the instance
            e.put()

            # This gets the (default) id of the entry
            e_id = str(e.key().id())


            self.redirect('/blog/' + e_id)
        else:
            error = "Title and content please"
            self.render_front(subject, content, error)
