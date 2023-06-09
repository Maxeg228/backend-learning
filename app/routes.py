from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Кто то'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        },
        {
            'author': {'username': 'Кто то'},
            'body': 'Йцук'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password_hash=form.password.data)
        if user.is_exist():
            flash('Login requested for user {}, remember_me={}'.format(
                form.username.data, form.remember_me.data))
            return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/CreateNews')
def create_news():
    form = LoginForm()
    return render_template('create_news.html', title='Create News', form=form)


@app.route('/Profile')
def profile():
    form = LoginForm()
    return render_template('Profile.html', title='Profile', form=form)