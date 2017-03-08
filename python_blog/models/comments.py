from google.appengine.ext import db


class Comments(db.Model):
    author = db.StringProperty(required=True)
    entry = db.IntegerProperty(required=True)
    comment = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def by_id(cls, uid):
        u = Comments.get_by_id(uid)
        return u

    @classmethod
    def by_entry(cls, entry_id, created):
        u = Comments.all().filter('entry =',
                                  entry_id).order(created).fetch(100)
        return u
