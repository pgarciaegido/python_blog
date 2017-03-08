from blog import Handler


class RHLogout(Handler):
    def get(self):
        self.response.headers.add_header('Set-Cookie', 'userid=; Path=/')
        self.redirect('/blog/signup')
