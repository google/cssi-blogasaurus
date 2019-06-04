import webapp2
import jinja2
import os

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

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/family', AboutMyFamilyHandler),
], debug=True)
