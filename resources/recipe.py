
from models.recipe import Recipe, recipe_list
from flask import request
from flask_restful import Resource
from http import HTTPStatus


class RecipeListResource(Resource):

    def get(self):

        data = []

        for recipe in recipe_list:
            if recipe.is_publish is True:
                data.append(recipe.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        recipe = Recipe(name=data['name'],
                        description=data['description'],
                        num_of_servings=data['num_of_servings'],
                        cook_time=data['cook_time'],
                        directions=data['directions'])

        recipe_list.append(recipe)

        return recipe.data, HTTPStatus.CREATED


class RecipeResource(Resources):

    def get(self, recipe_id):

        recipe = next(
            (item for item in recipes if item['id'] == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        return recipe.data, HTTPStatus.OK

    def put(self, recipe_id):

        data = request.get_json()

        recipe = next(
            (item for item in recipes if item['id'] == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.name = data['name']

        recipe.description = data['description']

        recipe.num_of_servings = data['num_of_servings']

        recipe.cook_time = data['cook_time']

        recipe.directions = data['directions']

        return recipe.data, HTTPStatus.OK
