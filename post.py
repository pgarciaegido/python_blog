from blog import Handler
import database

class Post(Handler):
    def get(self, product_id):
        entry = database.Entry.get_by_id(int(product_id))
        self.render("post.html", entry=entry)
