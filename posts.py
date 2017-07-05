# -*- coding: utf-8 -*-

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


INDEX = '''<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <title>Blogasaurus</title>
    <link rel="stylesheet" href="/static/style.css">
  </head>
  <body>
    <div id="content">
      <h1><a href="/">Blogasaurus</a></h1>
      <ul>
        <li><a href="all-about-me">All About Me</a></li>
        <li><a href="how-i-spent-my-summer-vacation">How I Spent My Summer Vacation</a></li>
      </ul>
    </div>
  </body>
</html>
'''


ALL_ABOUT_ME = '''<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <title>All About Me – Blogasaurus</title>
    <link rel="stylesheet" href="/static/style.css">
  </head>
  <body>
    <div id="content">
      <h1><a href="/">Blogasaurus</a></h1>
      <h2>All About Me</h2>
      <p>I live in Cambridge.  I like playing soccer.  I'm starting college in the fall as a freshman at UMass Boston.</p>
      <h3>Comments</h3>
      <div id="comments">
        <p id="no-comments">There are no comments on this post yet.</p>
      </div>
      <h3>Leave a Comment</h3>
      <form id="comment-form" action="javascript:void(0);">
        <textarea id="comment-content" name="content"></textarea>
        <input type="submit" value="Post Comment">
      </form>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="/static/comment.js"></script>
  </body>
</html>
'''


HOW_I_SPENT_MY_SUMMER_VACATION = '''<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <title>How I Spent My Summer Vacation – Blogasaurus</title>
    <link rel="stylesheet" href="/static/style.css">
  </head>
  <body>
    <div id="content">
      <h1><a href="/">Blogasaurus</a></h1>
      <h2>How I Spent My Summer Vacation</h2>
      <p>I read lots of books, worked at the local supermarket, and built a ridesharing app that works via smoke signals using the new Google Cloud Smoke Signals Service.</p>
      <h3>Comments</h3>
      <div id="comments">
        <p id="no-comments">There are no comments on this post yet.</p>
      </div>
      <h3>Leave a Comment</h3>
      <form id="comment-form" action="javascript:void(0);">
        <textarea id="comment-content" name="content"></textarea>
        <input type="submit" value="Post Comment">
      </form>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="/static/comment.js"></script>
  </body>
</html>
'''


ERROR_400 = '''<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <title>Bad Request – Blogasaurus</title>
    <link rel="stylesheet" href="/static/style.css">
  </head>
  <body>
    <div id="content">
      <h1><a href="/">Blogasaurus</a></h1>
      <h2>Bad Request</h2>
      <p>Something was wrong with your request, so it couldn’t be handled properly. That’s all we know.</p>
    </div>
  </body>
</html>
'''


ERROR_404 = '''<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <title>Not Found – Blogasaurus</title>
    <link rel="stylesheet" href="/static/style.css">
  </head>
  <body>
    <div id="content">
      <h1><a href="/">Blogasaurus</a></h1>
      <h2>Not Found</h2>
      <p>The page you’re looking for doesn’t exist on this website. You may have mistyped the URL or followed a broken link.</p>
    </div>
  </body>
</html>
'''


ERROR_500 = '''<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <title>Internal Server Error – Blogasaurus</title>
    <link rel="stylesheet" href="/static/style.css">
  </head>
  <body>
    <div id="content">
      <h1><a href="/">Blogasaurus</a></h1>
      <h2>Internal Server Error</h2>
      <p>Something went wrong, and we can’t show you the page you requested. We’re very sorry about this.</p>
    </div>
  </body>
</html>
'''
