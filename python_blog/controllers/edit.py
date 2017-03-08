# My modules
from handler import Handler
from python_blog.models.entry import Entry


class RHEdit(Handler):
    def get(self):
        user = self.get_user_cookie()
        # If user is not logged in
        if not user:
            self.redirect('/blog/login')

        else:
            post_id = self.request.query.split('=')[1]
            p = Entry.by_id(int(post_id))
            author = p.author

            if user.username != author:
                error = "Sorry, but you can only edit your own posts"
                self.render('error.html', error=error)

            else:
                subject = p.subject
                content = p.content

                self.render('edit.html', subject=subject, content=content,
                            post_id=post_id)

    def post(self):
        user = self.get_user_cookie()
        if not user:
            self.redirect('/blog/login')
        else:
            post_id = self.request.query.split('=')[1]
            p = Entry.by_id(int(post_id))
            author = p.author

            if user.username != author:
                self.redirect('/blog/login')
            else:
                subject = self.request.get('subject')
                content = self.request.get('content')

                # Getting post
                p.subject = subject
                p.content = content

                p.put()
                self.redirect('/blog/' + post_id)
