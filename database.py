from google.appengine.ext import db

### MODELS, DB TABLES
# Post
class Entry(db.Model):
    subject  = db.StringProperty(required = True)
    content  = db.TextProperty(required = True)
    author   = db.StringProperty(required = True)
    created  = db.DateTimeProperty(auto_now_add = True)
    likes    = db.IntegerProperty(required = True)
    liked_by = db.ListProperty(item_type = str) # --> List

    @classmethod
    def by_id(cls, pid):
        p = Entry.get_by_id(uid)
        return p

# User
class User(db.Model):
    username = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    email    = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        u = User.get_by_id(uid)
        return u

    @classmethod
    def by_username(cls, name):
        u = User.all().filter('username =', name).get()
        return u

class Comments(db.Model):
    author  = db.StringProperty(required = True)
    entry   = db.IntegerProperty(required = True)
    comment = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

    @classmethod
    def by_id(cls, uid):
        u = Coments.get_by_id(uid)
        return u

    @classmethod
    def by_entry(cls, entry_id):
        u = Comments.all().filter('entry =', entry_id).fetch(100)
        return u
