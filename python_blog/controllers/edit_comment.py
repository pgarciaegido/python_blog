# My modules
from handler import Handler
from python_blog.models.comments import Comments

import time


class RHEditComment(Handler):
    def get(self):
        # If user is not logged in
        if not self.request.cookies.get('userid'):
            self.redirect('/blog/login')

        else:
            user = self.get_user_cookie()
            comment_id = self.request.query.split('=')[1]
            # Comment instance from db
            c = Comments.by_id(int(comment_id))

            # if comment doesn't exist
            if not c:
                error = "This comment does not exist"
                self.render('error.html', error=error)

            else:
                author = c.author

                if user.username != author:
                    error = "Sorry, but you can only edit your own comments"
                    self.render('error.html', error=error)

                else:
                    post_id = c.entry
                    comment = c.comment
                    self.render('edit_comment.html', comment=comment,
                                post_id=post_id, comment_id=comment_id)

    def post(self):
        # If user is not logged in
        if not self.request.cookies.get('userid'):
            self.redirect('blog/login')
        else:
            comment_id = self.request.query.split('=')[1]
            # Getting comment from db
            c = Comments.by_id(int(comment_id))
            author = c.author
            user = self.get_user_cookie()

            if user.username != author:
                self.write('Access denied')

            else:
                # Getting new inputs on edition
                comment = self.request.get('comment')

                post_id = c.entry
                user = self.get_user_cookie()

                if c.comment == comment:
                    error = "Hey, your comment is the same!"
                    self.render('edit_comment.html', comment=comment,
                                post_id=post_id, comment_id=comment_id,
                                error=error)

                else:
                    # Setting comment
                    c.comment = comment
                    c.put()

                    time.sleep(0.1)
                    self.redirect('/blog/' + str(post_id))
