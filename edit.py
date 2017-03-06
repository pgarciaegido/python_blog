# My modules
from blog import Handler
from database import Entry
import logging

class Edit(Handler):
    def get(self):
        post_id = self.request.query.split('=')[1]
        post = Entry.get_by_id(int(post_id))
        subject = post.subject
        content = post.content
        self.render('edit.html', subject=subject, content=content, post_id=post_id, error="")

    def post(self):
        post_id = self.request.get('post')
        subject = self.request.get('subject')
        content = self.request.get('content')
        post = Entry.get_by_id(int(post_id))

        post.subject = subject
        post.content = content
        post.put()
        self.redirect('/blog/' + post_id)
