from google.appengine.ext import db


# Post
class Entry(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    author = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    likes = db.IntegerProperty(required=True)
    liked_by = db.ListProperty(item_type=str)  # --> List

    @classmethod
    def by_id(cls, pid):
        p = Entry.get_by_id(pid)
        return p
