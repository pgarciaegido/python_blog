# My modules
from handler import Handler
from python_blog.models.entry import Entry


class RHNew(Handler):
    def render_front(self, subject="", content="", author="", error=""):
        # Selects newpost template, with default empty strings for form inpts
        self.render("newpost.html", subject=subject, content=content,
                    author=author, error=error)

    def get(self):
        user = self.get_user_cookie()
        # Check cookies to see if user is logged
        if not user:
            self.redirect('/blog/signup')
        else:
            self.render_front()

    def post(self):
        user = self.get_user_cookie()
        if not user:
            self.redirect('/blog/login')
        else:
            # Get both the subject and the content
            subject = self.request.get('subject')
            content = self.request.get('content')
            author = user.username
            likes = 0

            if subject and content:
                # If both exist, create new db instance
                e = Entry(subject=subject, content=content,
                                   author=author, likes=likes)
                # This saves the instance
                e.put()

                # This gets the (default) id of the entry
                e_id = str(e.key().id())

                self.redirect('/blog/' + e_id)
            else:
                error = "Title and content please"
                self.render_front(subject, content, error)
