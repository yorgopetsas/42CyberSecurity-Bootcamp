import datetime


def check_recipe(name, last_update, creation_date, recipes_list):

    if not isinstance(name, str):
        print('Error Name Not String')

class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list
        check_recipe(self.name, self.last_update, self.creation_date, self.recipes_list)

    def __str__(self):
        return "Book " + self.name + " created"

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        name = name
        print()
    
    def get_recipe_by_name(self, recipe_type):
        """Get all recipe names for a given recipe_type """

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""


kniga = Book('kniga', datetime.datetime.now(), datetime.datetime.now(), {"starter": "salad", "lunch": "cordero", "dessert": "icecream"})

print(kniga)

# • name (str): nombre del libro,
# • last_update (datetime): la fecha de la última actualización,
# • creation_date (datetime): la fecha de creación,
# • recipes_list (dict): un diccionario con 3 claves: "starter", "lunch", "dessert".

# if not isinstance(last_update, int):
#     print('Error last_update Not INT')
# if not isinstance(creation_date, int):
#     print('Error creation_date Not INT')
# if not isinstance(recipes_list, list):
#     print('Error recipes_list Not List')
# if not isinstance(recipes_list, str) or not (recipes_list == "starter" or recipes_list == "lunch" or recipes_list == "dessert"):
#     print('Error recipes_list Not List')
# print(name, last_update, creation_date, recipes_list)