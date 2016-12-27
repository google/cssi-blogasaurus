import logging

import flask
from google.appengine.api import users

import posts


app = flask.Flask(__name__)


@app.route('/')
def index():
    user = users.get_current_user()
    if user:
        nickname = user.nickname()
        auth_url = users.create_logout_url(dest_url=flask.url_for('index'))
    else:
        nickname = None
        auth_url = users.create_login_url(dest_url=flask.url_for('index'))
    return flask.render_template(
        'index.html',
        nickname=nickname,
        is_admin=users.is_current_user_admin(),
        auth_url=auth_url,
        posts=posts.POSTS)


@app.route('/post/<int:post_id>')
def view_post(post_id):
    if 0 <= post_id - 1 < len(posts.POSTS):
        if users.get_current_user():
            sign_in_url = None
        else:
            sign_in_url = users.create_login_url(
                dest_url=flask.url_for('view_post', post_id=post_id))
        return flask.render_template(
            'view_post.html',
            post=posts.POSTS[post_id - 1],
            sign_in_url=sign_in_url)
    else:
        return flask.render_template('404.html'), 404


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
