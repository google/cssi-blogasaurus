import logging

import flask

import posts


app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html', posts=posts.POSTS)


@app.route('/post/<int:post_id>')
def view_post(post_id):
    if 0 <= post_id - 1 < len(posts.POSTS):
        return flask.render_template(
            'view_post.html', post=posts.POSTS[post_id - 1])
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
