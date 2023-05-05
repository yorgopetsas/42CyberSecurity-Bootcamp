

def check_recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):

    if not isinstance(name, str):
        print('Error Name Not String')
        exit()
    if not isinstance(cooking_lvl, int):
        print('Error cooking_lvl Not INT')
        exit()
    if cooking_lvl < 1 or cooking_lvl > 5:
        print('Error cooking_lvl Out Of Rage')
        exit()
    if not isinstance(cooking_time, int):
        print('Error cooking_time Not INT')
        exit()
    if cooking_time < 0:
        print('Error cooking_time Negative')
        exit()
    if not isinstance(description, str):
        print('Error Description Not String')
        exit()
    if not isinstance(recipe_type, str) or not (recipe_type == "entrante" or recipe_type == "comida" or recipe_type == "postre"):
        print('Error Description recipe_type String or not "entrante”, “comida” o “postre"')
        exit()


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        check_recipe(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)

    def __str__(self):
        """Return the string to print with the recipe info"""
        text = ""
        # return "The " + self.name + " recipe is a " + self.recipe_type + " type and the level " + str(self.cooking_lvl) + ", for this you need at least " + str(self.cooking_time) + " min to make it. The ingredients to do it are: " + str(self.ingredients) + ". " + str(self.description)
        return text

bocadillo = Recipe('bocadillo', 2, 10, ['jamón', 'pan', 'queso', 'tomate'], 'test_description', 'postre')

print(bocadillo)

#     name (str)
#     cooking_lvl (int): rango de 1 a 5
#     cooking_time (int): en minutos (sin números negativos)
#     ingredients (lista): lista de todos los ingredientes, cada uno representado por un string
#     description (str): descripción de la receta
#     recipe_type (str): puede ser “entrante”, “comida” o “postre”.