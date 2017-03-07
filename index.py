from google.appengine.ext import db

from blog import Handler
import logging

class Index(Handler):
    def render_index(self):
        #Gets all the news from db, and renders em
        entries = db.GqlQuery("SELECT * FROM Entry ORDER BY created DESC")
        logging.info(entries)
        self.render("index.html", entries=entries)

    def get(self):
        self.render_index()
