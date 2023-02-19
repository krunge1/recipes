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
        query = """SELECT * from Recipes
        ;
        """
        result = connectToMySQL(cls.db).query_db(query)

# Update


# Delete

#     @classmethod
#     def getAll(cls):
#         query = "SELECT * FROM dojos"
#         results = connectToMySQL(cls.db).query_db(query)
#         all_dojos = []
#         for row in results:
#             all_dojos.append(cls(row))
#         return all_dojos


#     @classmethod
#     def getOne (cls, data):
#         query = "SELECT * From ninjas LEFT JOIN dojos on ninjas.dojo_id = dojos. id WHERE dojos.id = %(id)s"
#         results = connectToMySQL(cls.db).query_db(query, data)
#         if results:
#             # print(results)
#             this_dojo = cls(results[0])
#             for row in results:
#                 this_dojo.ninjas.append(ninja.Ninja(row))
#             return this_dojo
#         return False

#     @classmethod
#     def read(cls, data):
#         query = """SELECT * from dojos
#         WHERE id = %(id)s
#         ;
#         """
#         result = connectToMySQL(cls.db).query_db(query, data)
#         return cls(result[0])

#     @classmethod
#     def create(cls, data):
#         query = "INSERT INTO dojos (name) VALUES (%(name)s);"
#         result = connectToMySQL(cls.db).query_db(query, data)
#         return result


    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s WHERE id=%(id)s;"
    #     result = connectToMySQL(cls.db).query_db(query, data)
    #     return result

    # @classmethod
    # def delete(cls, data):
    #     query = "DELETE FROM users WHERE id=%(id)s;"
    #     result = connectToMySQL(cls.db).query_db(query, data)
    #     return result

#establish the Class
#all SQL entry activity here