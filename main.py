import logging

import flask

import posts


app = flask.Flask(__name__)


@app.route('/')
def index():
    return posts.INDEX


@app.route('/all-about-me')
def all_about_me():
    return posts.ALL_ABOUT_ME


@app.route('/how-i-spent-my-summer-vacation')
def how_i_spent_my_summer_vacation():
    return posts.HOW_I_SPENT_MY_SUMMER_VACATION


@app.errorhandler(400)
def handle_400(error):
    return posts.ERROR_400, 400


@app.errorhandler(404)
def handle_404(error):
    return posts.ERROR_404, 404


@app.errorhandler(500)
def handle_500(error):
    logging.exception('An error occurred during a request.')
    return posts.ERROR_500, 500
