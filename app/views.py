"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime

def format_date_joined(unformatted_date):
    """
        When given a date as an argument, it will return the date
        formatted as: Month, Year.
    """
    formatted_date = unformatted_date.strftime("%B, %Y")

    return formatted_date

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Theron whorms")


@app.route('/profile/')
def profile():
    """Render the website's profile page."""

    # Data for a user
    name = "Theron Whorms"
    username = "twhorms12"
    parish, country = "St Catherine", "Jamaica"
    bio = "if you don't try you won't succeed"
    num_posts, num_follows, num_followers = 69, 1, 76,699

    # Retrieve current date
    unformatted_date= datetime.datetime.now()
    date = format_date_joined(unformatted_date)

    # Sends data to Profile Page
    return render_template('profile.html', name=name, username=username, parish=parish, country=country, date_joined=date, bio=bio, num_posts=num_posts, num_follows=num_follows, num_followers=num_followers)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
