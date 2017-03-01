from blog import Handler

class Welcome(Handler):
    def get(self):
        username = self.request.cookies.get('username').split('|')[0]
        self.write('welcome! your username is: %s ' % username)
