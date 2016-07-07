from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app import app
from .forms import LoginForm


@app.route('/')
@login_required
def index():
    user = {'name': 'Miguel'}  # fake user
    return render_template("index.html",
                           title='Home',
                           user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
      return redirect(url_for('index'))
    return render_template('login.html', 
                           title='Sign In',
                           form=form)