from mongoengine import *

class RecipeORM(Document):
    name = StringField()
    ingredients = ListField()
    prep_time = IntField()

    def print(self):
        print(f"{self.name} has {len(self.ingredients)} ingredients and takes {self.prep_time} minutes to make.")

class Recipe:
    def __init__(self, name, ingredients, prep_time, _id=None):
        if _id is not None:
            self._id = _id
        self.name = name
        self.ingredients = ingredients
        self.prep_time = prep_time