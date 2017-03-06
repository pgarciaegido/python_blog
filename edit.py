# My modules
from blog import Handler
from database import Entry
import logging

class Edit(Handler):
    def get(self):
        # If user is not logged in
        if not self.request.cookies.get('userid'):
            self.redirect('/blog/login')

        else:
            # Get postid from the query
            post_id = self.request.query.split('=')[1]
            # Find the result on db
            post = Entry.get_by_id(int(post_id))
            subject = post.subject
            content = post.content
            self.render('edit.html', subject=subject, content=content, post_id=post_id)

    def post(self):
        # Getting new inputs on edition
        post_id = self.request.get('post')
        subject = self.request.get('subject')
        content = self.request.get('content')
        # Getting
        post = Entry.get_by_id(int(post_id))

        post.subject = subject
        post.content = content
        post.put()
        self.redirect('/blog/' + post_id)
