# My modules
from blog import Handler
from models.entry import Entry


class RHEdit(Handler):
    def get(self):
        # If user is not logged in
        if not self.request.cookies.get('userid'):
            self.redirect('/blog/login')

        else:
            user = self.get_user_cookie()

            # Queries form looks like this:
            # p=IdNumberOfPost__a=username
            queries = self.request.query.split('__')
            author = queries[1].split('=')[1]

            if user.username != author:
                error = "Sorry, but you can only edit your own posts"
                self.render('error.html', error=error)

            else:
                # Get postid from the query
                post_id = queries[0].split('=')[1]

                # Find the result on db
                post = Entry.get_by_id(int(post_id))
                subject = post.subject
                content = post.content

                self.render('edit.html', subject=subject, content=content,
                            post_id=post_id)

    def post(self):
        # Getting new inputs on edition
        post_id = self.request.get('post')
        subject = self.request.get('subject')
        content = self.request.get('content')

        # Getting post
        post = Entry.get_by_id(int(post_id))

        post.subject = subject
        post.content = content

        post.put()
        self.redirect('/blog/' + post_id)
