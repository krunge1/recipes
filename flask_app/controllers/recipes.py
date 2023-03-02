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

@app.route('/recipes/<int:id>')
def show_one_recipes(id):
    return render_template('view_recipe.html', recipes=recipe.Recipe.get_one({'id': id}))

# Update
@app.route('/recipes/edit/<int:id>')
def show_edit_recipes(id):
    return render_template("edit_recipe.html", recipe=recipe.Recipe.get_one({'id': id}))

@app.route('/recipes/edit/<int:id>', methods=['POST'])
def edit_recipes(id):
    print(id)
    print(session['id'])
    if not recipe.Recipe.validate_recipe_registration_data(request.form):
        return redirect(f"/recipes/edit/{id}")
    data={
        "recipe_name": request.form['recipe_name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "date_cooked": request.form['date_cooked'],
        "under_thirty_minutes": request.form['under_thirty_minutes'],
        "user_id": session['id'],
        "id": id,
    }
    recipe.Recipe.update_recipe(data)
    return redirect('/recipes')

# Delete
@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    data={
        "id": id,
    }
    recipe.Recipe.delete(data)
    return redirect('/recipes')



