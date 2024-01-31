from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
