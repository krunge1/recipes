from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session
from flask_bcrypt import Bcrypt
import re
bcrypt = Bcrypt(app)

from flask_app.models import recipe

class Dojo:
    db = "recipes_schema"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []


# Create


# Read

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