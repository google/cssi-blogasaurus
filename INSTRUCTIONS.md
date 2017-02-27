# Instructions

1.  Create a single HTML page about yourself.  Use structured markup so that
    the elements on your page have the proper meaning.  Upload your one-page
    website to GitHub Pages so that it can be seen on a github.io subdomain.
2.  Create multiple HTML pages that are blog posts about whatever you want.
    Connect them together with hyperlinks, and create another HTML page to serve
    as a homepage/table of contents.  Create a CSS stylesheet to customize the
    appearance of your website and use it on each page.
3.  Use JavaScript and jQuery to add a comment system to your website, so that
    a user can write comments on posts and they appear at the bottom of the page
    when the user submits them.  (For now, it's okay for the comments to
    disappear when the user navigates away from the page and not be visible to
    anyone else.)
4.  Migrate your website from GitHub Pages to Google App Engine (Python Standard
    Environment).  Represent your HTML pages as strings in Python instead of
    static files, and serve them from a webapp2 application.  Serve your other
    resources (like stylesheets and scripts) as static files in App Engine.
    Deploy your website to an appspot.com subdomain.
5.  Migrate your HTML pages from hardcoded Python strings to Jinja2 templates.
    Eliminate all code duplication from your templates; if something is the same
    on multiple pages of your website, it should appear only once in your code.
    Generate your table of contents dynamically in Python code instead of
    writing it by hand.
