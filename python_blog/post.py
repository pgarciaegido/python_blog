# My modules
from blog import Handler
import database


class Post(Handler):
    def get(self, product_id):
        entry = database.Entry.get_by_id(int(product_id))
        if not entry:
            error = "Sorry, that post does not exist"
            self.render('error.html', error=error)
        else:
            comments = database.Comments.by_entry(int(product_id), 'created')
            self.render("post.html", entry=entry, comments=comments)
