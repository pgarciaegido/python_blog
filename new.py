from blog import Handler
import database

class New(Handler):
    def render_front(self, subject="", content="", error=""):
        # Selects newpost template, with default empry strings for form inpts
        self.render("newpost.html", subject=subject, content=content, error=error)

    def get(self):
        self.render_front()

    def post(self):
        # Get both the subject and the content
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            # If both exist, create new db instance
            e = database.Entry(subject = subject, content = content)
            # This saves the instance
            e.put()

            # This gets the (default) id of the entry
            e_id = str(e.key().id())


            self.redirect('/blog/' + e_id)
        else:
            error = "Title and content please"
            self.render_front(subject, content, error)
