import webapp2
import jinja2
import os
from models import Post
from models import Author

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/index.html')
        self.response.write(template.render())

class AboutMyFamilyHandler(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/about_my_family.html')
        self.response.write(template.render())

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/new_post.html')
        self.response.write(template.render())
    def post(self):
        title_input = self.request.get('title')
        content_input = self.request.get('content')
        name_input = self.request.get('name')

        blog_post = Post(title=title_input, content=content_input)
        blog_post.put()

        check_authors = Author.query(Author.username == name_input).fetch()
        # check_authors = [Author(username, posts), Author(), Author()]
        if len(check_authors) > 0:
            author = check_authors[0]
            author.posts.append(blog_post.key)
        else:
            author = Author(username=name_input, posts=[blog_post.key])

        author.put()

        blog_posts = []
        for blog_post_key in author.posts:
            blog_posts.append(blog_post_key.get())

        template_vars = {
            'username': name_input,
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
