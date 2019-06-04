from google.appengine.ext import ndb

class Post(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()

class Author(ndb.Model):
    username = ndb.StringProperty()
    posts = ndb.KeyProperty(kind="Post", repeated=True)
