import logging
import os
from os import path

import webapp2

import posts


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(posts.INDEX)


class AllAboutMeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(posts.ALL_ABOUT_ME)


class HowISpentMySummerVacationHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(posts.HOW_I_SPENT_MY_SUMMER_VACATION)


def handle_400(request, response, exception):
    response.set_status(400)
    response.write(posts.ERROR_400)


def handle_403(request, response, exception):
    response.set_status(403)
    response.write(posts.ERROR_403)


def handle_404(request, response, exception):
    response.set_status(404)
    response.write(posts.ERROR_404)


def handle_500(request, response, exception):
    logging.exception(exception)
    response.set_status(500)
    response.write(posts.ERROR_500)


app = webapp2.WSGIApplication(
    routes=[
        ('/', IndexHandler),
        ('/all-about-me', AllAboutMeHandler),
        ('/how-i-spent-my-summer-vacation', HowISpentMySummerVacationHandler),
    ],
    debug=(not
           os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/')))
app.error_handlers[400] = handle_400
app.error_handlers[403] = handle_403
app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500
