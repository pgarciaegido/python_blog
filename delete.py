# My modules
from blog import Handler
from database import Entry
import logging
import time

class Delete(Handler):

    def post(self):
        # If user is not logged in
        if not self.request.cookies.get('userid'):
            self.redirect('/blog/login')

        else:
            post_id = self.request.query.split('=')[1]
            post = Entry.get_by_id(int(post_id))
            post.delete()
            # When redirecting, db was still sending me the just deleted item
            # This workaround avoids that
            time.sleep(0.1)
            self.redirect('/blog')
