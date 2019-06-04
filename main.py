import webapp2
import jinja2
import os
from google.appengine.api import users
from models import Post
from models import Author

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            email = user.email()
            login_url = users.create_logout_url('/')
        else:
            email = None
            login_url = users.create_login_url('/')

        template = the_jinja_env.get_template('templates/index.html')
        self.response.write(template.render(
            user=user,
            email=email,
            is_admin=users.is_current_user_admin(),
            login_url=login_url))

class AboutMyFamilyHandler(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/about_my_family.html')
        self.response.write(template.render())

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/new_post.html')
        self.response.write(template.render())
    def post(self):
        user = users.get_current_user()
        nickname = user.nickname()

        title_input = self.request.get('title')
        content_input = self.request.get('content')

        blog_post = Post(title=title_input, content=content_input)
        blog_post.put()

        check_authors = Author.query(Author.username == nickname).fetch()
        # check_authors = [Author(username, posts), Author(), Author()]
        if len(check_authors) > 0:
            author = check_authors[0]
            author.posts.append(blog_post.key)
        else:
            author = Author(username=nickname, posts=[blog_post.key])

        author.put()

        blog_posts = []
        for blog_post_key in author.posts:
            blog_posts.append(blog_post_key.get())

        template_vars = {
            'nickname': nickname,
            'blog_posts': blog_posts
        }
        template = the_jinja_env.get_template(
            'templates/show_posts.html')
        self.response.write(template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/family', AboutMyFamilyHandler),
    ('/posts', BlogHandler),
], debug=True)
