
from flask import render_template, redirect, flash, url_for
from app import app
from app.forms import LoginForm
from app.fan import *

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Requested for user={}. remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title="SmartFan: Login", form=form)

@app.route('/')
@app.route('/fan', methods=['GET', 'POST'])
def fan():
    return render_template('fan.html')

@app.route('/fan/pwr', methods=['GET', 'POST'])
def fan_pwr():
    pwr()
    return redirect(url_for('fan'))

@app.route('/fan/1', methods=['GET', 'POST'])
def fan1():
    lowlow()
    return redirect(url_for('fan'))

@app.route('/fan/2', methods=['GET', 'POST'])
def fan2():
    low() 
    return redirect(url_for('fan'))

@app.route('/fan/3', methods=['GET', 'POST'])
def fan3():
    medium()
    return redirect(url_for('fan'))

@app.route('/fan/4', methods=['GET', 'POST'])
def fan4():
    high()
    return redirect(url_for('fan'))

@app.route('/yoda')
def yoda():
    return render_template('yoda.html')

"""
@app.route('/index')
def index():
    user = {'username': 'Patrick'}
    posts = [
        { 'author': {'username': 'John'}, 'body': 'Hello from portland'},
        { 'author': {'username': 'Larry'}, 'body': 'Fuck you John'}
    ]
    return render_template('hello.html', title="SmartFan", user=user, posts=posts)
"""

