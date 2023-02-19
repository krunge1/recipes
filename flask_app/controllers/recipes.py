from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import recipe


# Create
@app.route('/recipes/new')
def create_recipe():
    return render_template('new_recipe.html')

@app.route('/recipes/new', methods=['POST'])
def create_new_recipe():
    print(request.form)
    if recipe.Recipe.create(request.form):
        return redirect('/recipes')
    return redirect('/recipes/new')

# Read
@app.route('/recipes')
def show_all_recipes():
    return render_template('recipe_list.html', recipes=recipe.Recipe.get_all())



# Update


# Delete

# @app.route('/dojos')
# def dojos():
#     return render_template("dojo_summary.html", dojos = dojo.Dojo.getAll())

