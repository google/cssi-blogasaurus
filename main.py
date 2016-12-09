import logging

import flask
from google.appengine.api import users
from google.appengine.ext import ndb

import models


app = flask.Flask(__name__)


@app.route('/')
def index():
    is_signed_in = bool(users.get_current_user())
    if is_signed_in:
        auth_url = users.create_logout_url(flask.url_for('index'))
    else:
        auth_url = users.create_login_url()
    return flask.render_template(
        'index.html',
        is_signed_in=is_signed_in,
        is_admin=users.is_current_user_admin(),
        auth_url=auth_url,
        posts=models.Post.query().order(-models.Post.posted_at).fetch())


@app.route('/post/<post_id>')
def view_post(post_id):
    post = ndb.Key(urlsafe=post_id).get()
    if post:
        return flask.render_template('view_post.html', post=post)
    else:
        return flask.render_template('404.html'), 404


@app.route('/new-post')
def new_post():
    return flask.render_template('new_post.html')


@app.route('/submit-post', methods=['POST'])
def submit_post():
    post = models.Post(
        title=flask.request.form['title'],
        content=flask.request.form['content'])
    post_key = post.put()
    return flask.redirect(
        flask.url_for('view_post', post_id=post_key.urlsafe()))


@app.errorhandler(400)
def handle_400(error):
    return flask.render_template('400.html'), 400


@app.errorhandler(404)
def handle_404(error):
    return flask.render_template('404.html'), 404


@app.errorhandler(500)
def handle_500(error):
    logging.exception('An error occurred during a request.')
    return flask.render_template('500.html'), 500
