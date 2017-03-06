from blog import Handler
import database as db
import time
import logging

class Like(Handler):

    def post(self):
        # If user is not logged in
        if not self.request.cookies.get('userid'):
            self.redirect('/blog/login')

        else:
            username = self.request.get('username')
            post_id = self.request.query.split('=')[1]
            post = db.Entry.get_by_id(int(post_id))

            if any(username in u for u in post.liked_by):
                post.likes -= 1
                post.liked_by.remove(username)

            else:
                post.likes += 1
                post.liked_by.append(username)

            logging.info(post.liked_by)
            post.put()
            # When redirecting, db was still sending me the just deleted item
            # This workaround avoids that. (Documented at Stack Overflow)
            time.sleep(0.1)
            self.redirect('/blog')
