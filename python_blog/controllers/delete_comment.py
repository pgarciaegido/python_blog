# My modules
from handler import Handler
from python_blog.models.comments import Comments

import time


class RHDeleteComment(Handler):
    def post(self, comment_id):
        user = self.get_user_cookie()
        # If user is not logged in
        if not user:
            self.redirect('/blog/login')

        else:
            c = Comments.by_id(int(comment_id))
            author = c.author

            if user.username != author:
                error = 'Sorry, but you can only delete your own comments!'
                self.render('error.html', error=error)

            else:
                post_id = c.entry
                c.delete()
                # When redirecting, db was still sending me the just
                # deleted item. This workaround avoids that
                time.sleep(0.1)
                self.redirect('/blog/' + str(post_id))
