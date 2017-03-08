# My modules
from blog import Handler
from database import Comments

import time


class DeleteComment(Handler):
    def post(self):
        # If user is not logged in
        if not self.request.cookies.get('userid'):
            self.redirect('/blog/login')

        else:
            user = self.get_user_cookie()
            author = self.request.get('author')

            if user.username != author:
                error = 'Sorry, but you can only delete your own comments!'
                self.render('error.html', error=error)

            else:
                comment_id = self.request.query.split('=')[1]
                comment = Comments.get_by_id(int(comment_id))

                comment.delete()
                # When redirecting, db was still sending me the just deleted
                # item. This workaround avoids that
                time.sleep(0.1)
                self.redirect('/blog/')
