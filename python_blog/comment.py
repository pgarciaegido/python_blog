# My modules
from blog import Handler
from models.entry import Entry
from models.comments import Comments

import time


class RHComment(Handler):
    def post(self):
        user = self.get_user_cookie()
        if not user:
            self.redirect('/blog/login')
        else:
            entry = self.request.query.split('=')[1]
            e = Entry.by_id(int(entry))
            comment = self.request.get('comment')

            c = Comments(author=user.username, entry=int(entry),
                         comment=comment)
            c.put()

            time.sleep(0.1)
            self.redirect('/blog/' + entry)
