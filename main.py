import logging

import flask
from google.appengine.api import users
from google.appengine.ext import ndb

import models


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
        posts=models.Post.query().order(-models.Post.posted_at).fetch())


@app.route('/post/<post_id>')
def view_post(post_id):
    post_key = ndb.Key(urlsafe=post_id)
    post = post_key.get()
    if post:
        comments = (models.Comment.query(models.Comment.post == post_key)
                    .order(models.Comment.posted_at).fetch())
        if users.get_current_user():
            sign_in_url = None
        else:
            sign_in_url = users.create_login_url(
                dest_url=flask.url_for('view_post', post_id=post_id))
        return flask.render_template(
            'view_post.html', post=post, comments=comments,
            sign_in_url=sign_in_url)
    else:
        return flask.render_template('404.html'), 404


@app.route('/new-post')
def new_post():
    if not users.is_current_user_admin():
        return flask.render_template('403.html'), 403
    return flask.render_template('new_post.html')


@app.route('/submit-post', methods=['POST'])
def submit_post():
    if not users.is_current_user_admin():
        return flask.render_template('403.html'), 403
    post = models.Post(
        title=flask.request.form['title'],
        content=flask.request.form['content'])
    post_key = post.put()
    return flask.redirect(
        flask.url_for('view_post', post_id=post_key.urlsafe()))


@app.route('/submit-comment', methods=['POST'])
def submit_comment():
    user = users.get_current_user()
    if not user:
        return flask.render_template('403.html'), 403
    post_key = ndb.Key(urlsafe=flask.request.form['post_id'])
    if not post_key.get():
        return flask.render_template('400.html'), 400
    author = models.Author(nickname=user.nickname(), email=user.email())
    comment = models.Comment(
        post=post_key, author=author, content=flask.request.form['content'])
    comment.put()
    best_match = flask.request.accept_mimetypes.best_match(
        ['application/json', 'text/html'])
    if (best_match == 'application/json' and
        flask.request.accept_mimetypes[best_match] >
        flask.request.accept_mimetypes['text/html']):
        return flask.jsonify(nickname=author.nickname, email=author.email)
    else:
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
