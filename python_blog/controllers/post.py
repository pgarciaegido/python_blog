# My modules
from blog import Handler
from python_blog.models.entry import Entry
from python_blog.models.comments import Comments


class RHPost(Handler):
    def get(self, product_id):
        entry = Entry.get_by_id(int(product_id))
        if not entry:
            error = "Sorry, that post does not exist"
            self.render('error.html', error=error)
        else:
            comments = Comments.by_entry(int(product_id), 'created')
            self.render("post.html", entry=entry, comments=comments)
