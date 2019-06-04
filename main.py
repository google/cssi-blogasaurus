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
        # Use the user input to create a new blog post
        title_input = self.request.get('title')
        content_input = self.request.get('content')

        blog_post = Post(title=title_input, content=content_input)
        blog_post.put()

        # Get the Author if one already exists with that name, or create one
        # otherwise. Add the new blog post to their list of posts.
        # Note: if you didn't create an Author Model, your `post` method will
        # look very different. See below for an alternative.
        check_authors = Author.query(Author.username == nickname).fetch()
        if len(check_authors) > 0:
            author = check_authors[0]
            author.posts.append(blog_post.key)
        else:
            author = Author(username=nickname, posts=[blog_post.key])

        author.put()

        # Create a list of all the blog post objects by the given author
        blog_posts = []
        for blog_post_key in author.posts:
            blog_posts.append(blog_post_key.get())

        # Render the template
        template_vars = {
            'nickname': nickname,
            'blog_posts': blog_posts
        }
        template = the_jinja_env.get_template(
            'templates/show_posts.html')
        self.response.write(template.render(template_vars))

    ################################################################
    # This is an alternative way of completing this exercise that doesn't
    # use the Author Model.
    # def post(self):
    #     # Get a list of all previously created blog posts
    #     blog_posts = Post.query().fetch()
    #
    #     # Use the user input to create a new blog post
    #     title_input = self.request.get('title')
    #     content_input = self.request.get('content')
    #     name_input = self.request.get('name')
    #
    #     blog_post = Post(title=title_input,
    #                      content=content_input,
    #                      author=name_input)
    #     blog_post.put()
    #
    #     # Add the new post to the beginning of our already-queried list of
    #     # posts
    #     blog_posts.insert(0, blog_post)
    #
    #     # Render the template
    #     template_vars = {
    #         'username': name_input,
    #         'blog_posts': blog_posts
    #     }
    #     template = the_jinja_env.get_template(
    #         'templates/show_posts.html')
    #     self.response.write(template.render(template_vars))
    ################################################################

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/family', AboutMyFamilyHandler),
    ('/posts', BlogHandler),
], debug=True)
