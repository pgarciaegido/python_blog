# My modules
from handler import Handler
from python_blog.models.entry import Entry

# Built-in
import time


class RHDelete(Handler):
    def post(self, post_id):
        user = self.get_user_cookie()
        # If user is not logged in
        if not user:
            self.redirect('/blog/login')

        else:
            p = Entry.get_by_id(int(post_id))

            if not p:
                self.redirect('/blog')

            else:
                author = p.author

                if user.username != author:
                    error = 'Sorry, but you can only delete your own posts!'
                    self.render('error.html', error=error)

                else:
                    p.delete()
                    # When redirecting, db was still sending me the just
                    # deleted item. This workaround avoids that
                    time.sleep(0.1)
                    self.redirect('/blog')
