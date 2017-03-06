# My modules
from blog import Handler
from database import Entry
import logging

class Delete(Handler):
    # def render_front(self, template, subject="", content="", error=""):
    #     post_id = self.request.query.split('=')[1]
    #     post = Entry.get_by_id(int(post_id))
    #     subject = post.subject
    #     content = post.content

    def post(self):
        post_id = self.request.query.split('=')[1]
        post = Entry.get_by_id(int(post_id))
        post.delete()
