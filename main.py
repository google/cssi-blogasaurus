# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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


def handle_404(request, response, exception):
    response.set_status(404)
    response.write(posts.ERROR_404)


def handle_500(request, response, exception):
    logging.exception(exception)
    response.set_status(500)
    response.write(posts.ERROR_500)


production = os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/')
app = webapp2.WSGIApplication(
    routes=[
        ('/', IndexHandler),
        ('/all-about-me', AllAboutMeHandler),
        ('/how-i-spent-my-summer-vacation', HowISpentMySummerVacationHandler),
    ],
    debug=(not production))
app.error_handlers[400] = handle_400
app.error_handlers[404] = handle_404
if production:
    app.error_handlers[500] = handle_500
