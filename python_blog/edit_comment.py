# My modules
from blog import Handler
from database import Comments

import time

class EditComment(Handler):
    def get(self):
        # If user is not logged in
        if not self.request.cookies.get('userid'):
            self.redirect('/blog/login')

        else:
            user = self.get_user_cookie()

            # Queries form looks like this:
            # p=IdNumberOfPost__a=username
            queries = self.request.query.split('__')
            author  = queries[1].split('=')[1]

            if user.username != author:
                error = "Sorry, but you can only edit your own comments"
                self.render('error.html', error=error)

            else:
                # Get comment id from the query
                comment_id = queries[0].split('=')[1]
                post_id    = queries[2].split('=')[1]

                # Find the result on db
                c = Comments.get_by_id(int(comment_id))
                comment = c.comment

                self.render('edit_comment.html', comment=comment,
                                                 comment_id=comment_id,
                                                 post_id=post_id)

    def post(self):
        # Getting new inputs on edition
        comment_id = self.request.get('comment_id')
        post_id    = self.request.get('post_id')
        comment    = self.request.get('comment')

        # Getting comment
        c = Comments.by_id(int(comment_id))
        c.comment = comment
        c.put()

        time.sleep(0.1)
        self.redirect('/blog/' + post_id)
