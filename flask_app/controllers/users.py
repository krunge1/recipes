from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user


# Create
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/', methods=["POST"])
def createUser():
    if request.form["register"] == "register":
        #run registration activity
        if user.User.create(request.form):
            return redirect('/recipes')
        return redirect('/')
    else:
        if user.User.login(request.form):
            return redirect('/recipes')
        else:
            return redirect('/')
    

# Read
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# Update


# Delete

# @app.route('/dojos')
# def dojos():
#     return render_template("dojo_summary.html", dojos = dojo.Dojo.getAll())

