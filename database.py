from google.appengine.ext import db

# Creates a new table(?). This is the schema.
class Entry(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class User(db.Model):
    username = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        u = User.get_by_id(uid)
        return u

    @classmethod
    def by_username(cls, name):
        u = User.all().filter('username =', name).get()
        return u
