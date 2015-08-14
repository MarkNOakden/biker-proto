from flask import Flask, redirect, request

from google.appengine.api import users

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def home_page():
    """Return a friendly HTTP greeting."""
    # Checks for active Google account session
    user = users.get_current_user()

    if user:
        return "Hello " + user.nickname() + " bikeR is GO! (" + user.user_id() + ")"
    else:
        return redirect(users.create_login_url(request.url))

@app.route('/config')
def config_page():
    return "config page"

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
