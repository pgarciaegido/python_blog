# My modules
from handler import Handler
from python_blog.models.entry import Entry
from python_blog.models.comments import Comments

import time


class RHComment(Handler):
    def post(self, post_id):
        user = self.get_user_cookie()
        if not user:
            self.redirect('/blog/login')
        else:
            e = Entry.by_id(int(post_id))

            if not e:
                self.redirect('/blog')

            else:
                comment = self.request.get('comment')

                c = Comments(author=user.username, entry=int(post_id),
                             comment=comment)
                c.put()

                time.sleep(0.1)
                self.redirect('/blog/' + post_id)
