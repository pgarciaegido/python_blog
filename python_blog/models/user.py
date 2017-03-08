from google.appengine.ext import db


# User
class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        u = User.get_by_id(uid)
        return u

    @classmethod
    def by_username(cls, name):
        u = User.all().filter('username =', name).get()
        return u
