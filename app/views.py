from flask import render_template
from flask_login import login_required, current_user
from flask_cache import Cache
from flask import Flask
from .util import check_expired
from . import app

app = Flask()

cache = Cache(app)

@decorator_function
def decorated():
	pass

@app.route('/')
@cache.cached(timeout=60)
def index():
	return render_template(
		'index.html',
		latest_posts=latest_posts,
		recent_users=recent_users,
		recent_photos=recent_photos
	)

@app.route('/dashboard')
@login_required
def account():
	return render_template("account.html")

@app.route('/use_app')
@login_required
@check_expired
def use_app():
	"""Use the app."""
	return render_template('use_app.html')

@app.route('/account/billing')
@login_required
def account_billing():
	"""Update billing info."""
	return render_template('account/billing.html')

@app.route('/user/id/<int:user_id>')
def profile(user_id):
	pass

@app.route('/r/<list:subreddits>')
def subreddit_home(subreddits):
	"""show all of the posts for the given subreddits."""
	posts = []
	for subreddit in subreddits:
		posts.extend(subreddit.posts)

	return render_template('/r/index.html', posts=posts)