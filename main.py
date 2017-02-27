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

import json
import logging
import os
from os import path

from google.appengine.api import users
import jinja2
import webapp2

import posts


template_dir = path.join(path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            auth_url = users.create_logout_url(dest_url='/')
        else:
            nickname = None
            auth_url = users.create_login_url(dest_url='/')
        self.response.write(jinja_environment.get_template('index.html').render(
            nickname=nickname,
            is_admin=users.is_current_user_admin(),
            auth_url=auth_url,
            posts=posts.POSTS))


class ViewPostHandler(webapp2.RequestHandler):
    def get(self):
        try:
            post_id = int(self.request.get('id'))
        except ValueError:
            webapp2.abort(400)
        else:
            if 0 <= post_id - 1 < len(posts.POSTS):
                if users.get_current_user():
                    sign_in_url = None
                else:
                    sign_in_url = users.create_login_url(
                        dest_url=('/view-post?id=' + str(post_id)))
                self.response.write(
                    jinja_environment.get_template('view_post.html').render(
                        post=posts.POSTS[post_id - 1], sign_in_url=sign_in_url))
            else:
                webapp2.abort(404)


def handle_400(request, response, exception):
    response.set_status(400)
    response.write(jinja_environment.get_template('400.html').render())


def handle_403(request, response, exception):
    response.set_status(403)
    response.write(jinja_environment.get_template('403.html').render())


def handle_404(request, response, exception):
    response.set_status(404)
    response.write(jinja_environment.get_template('404.html').render())


def handle_500(request, response, exception):
    logging.exception(exception)
    response.set_status(500)
    response.write(jinja_environment.get_template('500.html').render())


production = os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/')
app = webapp2.WSGIApplication(
    routes=[
        ('/', IndexHandler),
        ('/view-post', ViewPostHandler),
    ],
    debug=(not production))
app.error_handlers[400] = handle_400
app.error_handlers[403] = handle_403
app.error_handlers[404] = handle_404
if production:
    app.error_handlers[500] = handle_500
