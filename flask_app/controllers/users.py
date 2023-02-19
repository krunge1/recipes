from flask_app import app
from flask import render_template, redirect, request, session, flash
# from flask_app.models import **NAME OF CLASS MODEL FILE

@app.route('/')
def login():
    return render_template('login.html')

# Create


# Read

# Update


# Delete

# @app.route('/dojos')
# def dojos():
#     return render_template("dojo_summary.html", dojos = dojo.Dojo.getAll())

