# Blogasaurus

This is a simple web application that hosts a blog with comments. It is part of
the educational curriculum used at Google's [Computer Science Summer
Institute](https://edu.google.com/resources/programs/computer-science-summer-institute/).

Students work on this app in [multiple stages](INSTRUCTIONS.md). The code for
each stage is available as a separate branch in this Git repository.

You are currently viewing stage 7, which focuses on persistent data storage. A
[live demo](https://cssi-blogasaurus-stage-7.appspot.com/) is available. Note
that you cannot sign in as admin in the demo and all comments are deleted every
15 minutes.

This app runs on the [Google App Engine Python Standard
Environment](https://cloud.google.com/appengine/docs/standard/python/). To run
it locally, [install the Google Cloud
SDK](https://cloud.google.com/appengine/docs/standard/python/download), then run
`dev_appserver.py app.yaml`.

This is not an official Google product.
