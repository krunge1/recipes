from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session
from flask_bcrypt import Bcrypt
import re
bcrypt = Bcrypt(app)

from flask_app.models import user, recipe

class Recipe:
    db = "recipes_schema"

    def __init__(self,data):
        self.id = data['id']
        self.recipe_name = data['recipe_name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_thirty_minutes = data['under_thirty_minutes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.posted = None


# Create
    @classmethod
    def create(cls, data):
        if not cls.validate_recipe_registration_data(data):
            return False
        query = "INSERT INTO recipes (recipe_name, description, instructions, date_cooked, under_thirty_minutes, user_id) VALUES (%(recipe_name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_thirty_minutes)s, %(user_id)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @staticmethod # VALIDATE user
    def validate_recipe_registration_data(data): 
        is_valid = True
        if len(data['recipe_name'])<3:
            flash('Recipe name must be at least three characters long.')
            is_valid = False
        if len(data['description'])<3:
            flash('Description must be at least three characters long.')
            is_valid = False
        if len(data['instructions'])<3:
            flash('Instructions must be at least three characters long.')
            is_valid = False
        return is_valid

# Read
    @classmethod
    def get_one(cls, data):
        query = """SELECT * from recipes
        WHERE id = %(id)s
        ;
        """
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_all(cls):
        query = """SELECT * from recipes 
        LEFT JOIN users on recipes.user_id = users.id
        ;
        """
        results = connectToMySQL(cls.db).query_db(query)
        if not results: 
            return False
        all_recipes = []
        for row in results:
            this_recipe = cls(row)
            user_data = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at'],
            }
            chef = user.User(user_data)
            this_recipe.posted = chef
            all_recipes.append(this_recipe)
        # print(row)
        # print(this_recipe.posted.first_name)
        return all_recipes

    @classmethod
    def get_one(cls, data):
        query = """SELECT * from recipes 
        LEFT JOIN users on recipes.user_id = users.id
        WHERE recipes.id = %(id)s
        ;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return False    
        row = results[0]
        this_recipe = cls(row)
        user_data = {
            "id": row['users.id'],
            "first_name": row['first_name'],
            "last_name": row['last_name'],
            "email": row['email'],
            "password": row['password'],
            "created_at": row['users.created_at'],
            "updated_at": row['users.updated_at'],
            }
        this_recipe.posted = user.User(user_data)
        return this_recipe

# Update
    @classmethod
    def update_recipe(cls, data):
        if not cls.validate_recipe_registration_data(data):
            return False
        query = "UPDATE recipes SET recipe_name=%(recipe_name)s, description=%(description)s, instructions=%(instructions)s, date_cooked=%(date_cooked)s, under_thirty_minutes=%(under_thirty_minutes)s, user_id=%(user_id)s WHERE id=%(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

# Delete
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

