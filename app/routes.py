from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sqla
from app import db
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'The industrial revolution and its consequences.'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'This will negatively affect the trout population.'
        },
        {
            'author': {'username': 'Colin'},
            'body': 'This Flask business is kinda lit.'
        }
    ]

    return render_template('index.html', user=user, posts=posts)


# This does not work :(
@app.route('/ragnar')
def ragnar():
    return "Ragnar is inherently underpwered."


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sqla.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
