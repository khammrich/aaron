"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import current_app as app
from .nav import nav


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        nav=nav
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.',
        nav=nav
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About Aaron Moore',
        year=datetime.now().year,
        message='Get to know Aaron Moore',
        nav=nav
    )


@app.route('/bob')
def cartest():
    """Renders the about page."""
    return render_template(
        'bob.html',
        title='caroseltester',
        year=datetime.now().year,
        message='test',
        nav=nav
    )


@app.route('/search')
def search():
    """Renders the about page."""
    return render_template(
        'search.html',
        title='Search Seattle Area',
        year=datetime.now().year,
        message='Pick a Search Area',
        nav=nav
    )


@app.route('/search2')
def search2():
    """Renders the about page."""
    return render_template(
        'search2.html',
        title='Search Seattle Area',
        year=datetime.now().year,
        message='Pick a Search Area',
        nav=nav
    )


@app.route('/social')
def social():
    """Renders the about page."""
    return render_template(
        'social.html',
        title='socialicons',
        year=datetime.now().year,
        message='test',
        nav=nav
    )