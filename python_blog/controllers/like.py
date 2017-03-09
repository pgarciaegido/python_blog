from handler import Handler
from python_blog.models.entry import Entry

import time


class RHLike(Handler):
    def post(self, post_id):
        user = self.get_user_cookie()
        # If user is not logged in
        if not user:
            self.redirect('/blog/login')

        else:
            post = Entry.by_id(int(post_id))
            author = post.author
            username = user.username

            if username == author:
                error = 'Sorry, but you cannot like your own posts!'
                self.render('error.html', error=error)
            else:
                # If username is part of liked_by list
                # Unlike
                if any(username in u for u in post.liked_by):
                    post.liked_by.remove(username)

                # Like
                else:
                    post.liked_by.append(username)

                post.put()
                # When redirecting, db was still sending me the just
                # deleted item
                # This workaround avoids that. (Documented at Stack Overflow)
                time.sleep(0.1)
                self.redirect('/blog')
