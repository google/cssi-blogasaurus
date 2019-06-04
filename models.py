from google.appengine.ext import ndb

class Post(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()

# Having a second Model for Author wasn't required for this exercise (you can
# add an ndb.StringProperty called `author` to Post instead), but it's good
# practice to separate out data that is semantically discreet into its own
# Model-- meaning, `author` is different from `title` and `content` because
# authors exist independently from a post, but titles and content do not.
class Author(ndb.Model):
    username = ndb.StringProperty()
    posts = ndb.KeyProperty(kind="Post", repeated=True)
