# My modules
from blog import Handler
import database

import time

class Comment(Handler):
    def post(self):
        query  = self.request.query.split('__')
        entry  = query[0].split('=')[1]
        author = query[1].split('=')[1]

        comment = self.request.get('comment')

        c = database.Comments(author=author, entry=int(entry), comment=comment)
        c.put()

        time.sleep(0.1)
        self.redirect('/blog/' + entry)
