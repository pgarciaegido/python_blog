# My modules
from blog import Handler
import database

class Comment(Handler):
    def post(self):
        query  = self.request.query.split('__')
        entry  = query[0].split('=')[1]
        author = query[1].split('=')[1]

        comment = self.request.get('comment')

        c = database.Comments(author=author, entry=int(entry), comment=comment)
        c.put()

        self.redirect('/blog/' + entry)
