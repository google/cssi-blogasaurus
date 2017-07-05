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
from google.appengine.ext import ndb
import jinja2
import webapp2

import models


template_dir = path.join(path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            email = user.email()
            auth_url = users.create_logout_url(dest_url='/')
        else:
            email = None
            auth_url = users.create_login_url(dest_url='/')
        self.response.write(jinja_environment.get_template('index.html').render(
            email=email,
            is_admin=users.is_current_user_admin(),
            auth_url=auth_url,
            posts=models.Post.query().order(-models.Post.posted_at).fetch()))


class ViewPostHandler(webapp2.RequestHandler):
    def get(self):
        post_id = self.request.get('id')
        post_key = ndb.Key(urlsafe=post_id)
        post = post_key.get()
        if post:
            comments = (models.Comment.query(models.Comment.post == post_key)
                        .order(models.Comment.posted_at).fetch())
            if users.get_current_user():
                sign_in_url = None
            else:
                sign_in_url = users.create_login_url(
                    dest_url=('/view-post?id=' + post_id))
            self.response.write(
                jinja_environment.get_template('view_post.html').render(
                    post=post, comments=comments, sign_in_url=sign_in_url))
        else:
            webapp2.abort(404)


class NewPostHandler(webapp2.RequestHandler):
    def get(self):
        if users.is_current_user_admin():
            self.response.write(
                jinja_environment.get_template('new_post.html').render())
        else:
            webapp2.abort(403)


class SubmitPostHandler(webapp2.RequestHandler):
    def post(self):
        if users.is_current_user_admin():
            title = self.request.get('title')
            content = self.request.get('content')
            if title and content:
                post_key = models.Post(title=title, content=content).put()
                return webapp2.redirect('/view-post?id=' + post_key.urlsafe())
            else:
                webapp2.abort(400)
        else:
            webapp2.abort(403)


class SubmitCommentHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if user:
            post_key = ndb.Key(urlsafe=self.request.get('post_id'))
            content = self.request.get('content')
            if post_key.get() and content:
                comment = models.Comment(
                    post=post_key, author_email=user.email(), content=content)
                comment.put()
                if ('application/json' in
                    self.request.headers.get('Accept', '').lower()):
                    self.response.write(json.dumps({'email': user.email()}))
                else:
                    return webapp2.redirect(
                        '/view-post?id=' + post_key.urlsafe())
            else:
                webapp2.abort(400)
        else:
            webapp2.abort(403)


class ClearCommentsHandler(webapp2.RequestHandler):
    def get(self):
        if (users.is_current_user_admin() or
            self.request.headers.get('X-Appengine-Cron') == 'true'):
            for comment_key in models.Comment.query().iter(keys_only=True):
                comment_key.delete()
            self.response.set_status(204)
        else:
            webapp2.abort(403)


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
        ('/new-post', NewPostHandler),
        ('/submit-post', SubmitPostHandler),
        ('/submit-comment', SubmitCommentHandler),
        ('/clear-comments', ClearCommentsHandler),
    ],
    debug=(not production))
app.error_handlers[400] = handle_400
app.error_handlers[403] = handle_403
app.error_handlers[404] = handle_404
if production:
    app.error_handlers[500] = handle_500
