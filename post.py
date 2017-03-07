# My modules
from blog import Handler
import database
import logging

class Post(Handler):
    def get(self, product_id):
        entry    = database.Entry.get_by_id(int(product_id))
        comments = database.Comments.by_entry(int(product_id))
        logging.info(comments)
        self.render("post.html", entry=entry, comments=comments)
