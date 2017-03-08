from blog import Handler
import database as db

import time


class Like(Handler):

    def post(self):
        # If user is not logged in
        if not self.request.cookies.get('userid'):
            self.redirect('/blog/login')

        else:
            username = self.request.get('username')
            author = self.request.get('author')

            if username == author:
                error = 'Sorry, but you cannot like your own posts!'
                self.render('error.html', error=error)
            else:
                post_id = self.request.query.split('=')[1]
                post = db.Entry.get_by_id(int(post_id))

                # If username is part of liked_by list
                # Unlike
                if any(username in u for u in post.liked_by):
                    post.likes -= 1
                    post.liked_by.remove(username)

                # Like
                else:
                    post.likes += 1
                    post.liked_by.append(username)

                post.put()
                # When redirecting, db was still sending me the just
                # deleted item
                # This workaround avoids that. (Documented at Stack Overflow)
                time.sleep(0.1)
                self.redirect('/blog')
