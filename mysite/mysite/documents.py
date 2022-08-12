from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from recipes.models import Recipe, RecipeType

@registry.register_document
class UserDocument(Document):
    class Index:
        name = 'users'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
        ]


@registry.register_document
class CategoryDocument(Document):
    id = fields.IntegerField()

    class Index:
        name = 'categories'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = RecipeType
        fields = [
            'recipe_type_name',
        ]


@registry.register_document
class RecipeDocument(Document):
    # author = fields.ObjectField(properties={
    #     'id': fields.IntegerField(),
    #     'first_name': fields.TextField(),
    #     'last_name': fields.TextField(),
    #     'username': fields.TextField(),
    # })
    # categories = fields.ObjectField(properties={
    #     'id': fields.IntegerField(),
    #     'name': fields.TextField(),
    #     'description': fields.TextField(),
    # })
    # type = fields.TextField(attr='type_to_string')

    class Index:
        name = 'recipes'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Recipe
        fields = [
            'recipe_name',
            'recipe_description'
        ]