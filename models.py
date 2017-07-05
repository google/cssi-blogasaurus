#!/usr/bin/python
#
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

from google.appengine.ext import ndb


class Post(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    posted_at = ndb.DateTimeProperty(auto_now_add=True)


def get_all_posts():
    return Post.query().order(-Post.posted_at).fetch()


def get_post_by_id(post_id):
    return ndb.Key(urlsafe=post_id).get()


def create_post(title, content):
    return Post(title=title, content=content).put().urlsafe()


class Comment(ndb.Model):
    post = ndb.KeyProperty(kind=Post)
    author_email = ndb.StringProperty()
    content = ndb.TextProperty()
    posted_at = ndb.DateTimeProperty(auto_now_add=True)


def get_comments_by_post_id(post_id):
    return (Comment.query(Comment.post == ndb.Key(urlsafe=post_id))
            .order(Comment.posted_at).fetch())


def create_comment(post_id, author_email, content):
    return Comment(post=ndb.Key(urlsafe=post_id), author_email=author_email,
                   content=content).put().urlsafe()


def delete_all_comments():
    for comment_key in Comment.query().iter(keys_only=True):
        comment_key.delete()
