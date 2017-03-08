# My modules
from blog import Handler
from python_blog.models.entry import Entry

# Built-in
import time


class RHDelete(Handler):
    def post(self):
        # If user is not logged in
        if not self.request.cookies.get('userid'):
            self.redirect('/blog/login')

        else:
            user = self.get_user_cookie()
            author = self.request.get('author')

            if user.username != author:
                error = 'Sorry, but you can only delete your own posts!'
                self.render('error.html', error=error)

            else:
                post_id = self.request.query.split('=')[1]
                post = Entry.get_by_id(int(post_id))

                post.delete()
                # When redirecting, db was still sending me the just deleted
                # item. This workaround avoids that
                time.sleep(0.1)
                self.redirect('/blog')
