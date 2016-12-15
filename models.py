from google.appengine.ext import ndb


class Post(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    posted_at = ndb.DateTimeProperty(auto_now_add=True)


class Author(ndb.Model):
    nickname = ndb.StringProperty()
    email = ndb.StringProperty()


class Comment(ndb.Model):
    post = ndb.KeyProperty(kind=Post)
    author = ndb.StructuredProperty(Author)
    content = ndb.TextProperty()
    posted_at = ndb.DateTimeProperty(auto_now_add=True)
