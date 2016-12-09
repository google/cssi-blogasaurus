from google.appengine.ext import ndb


class Post(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    posted_at = ndb.DateTimeProperty(auto_now_add=True)


# class Comment(ndb.Model):
#     post = ndb.KeyProperty(kind=Post)
#     author_id = ndb.StringProperty()
#     body = ndb.TextProperty()
#     posted_at = ndb.DateTimeProperty(auto_now_add=True)
