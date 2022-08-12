from django.test import TestCase, Client
import unittest

class RecipeTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_recipe_list(self):
        response = self.Client().get('/api/recipes')
        assert response.status_code == 200

    def test_recipe_types_list(self):
        response = self.client.get('/api/recipe_types')
        assert response.status_code == 200

    def test_get_recipe_by_id(self):
        response = self.client.get('/api/recipes/1')
        assert response.status_code == 200

    def test_post_recipe_duplicate(self):
        response = self.client.post('/api/recipes', {
            "recipe_name": "plov",
            "recipe_description": "123",
            "recipe_type": 5
        })
        assert response.status_code == 400
