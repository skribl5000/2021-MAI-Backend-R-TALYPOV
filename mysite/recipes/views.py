from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from recipes.models import Recipe, RecipeType
from rest_framework import viewsets
from .serializers import RecipeSerializer, RecipeTypeSerializer
from django.contrib.auth.decorators import login_required

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer


class RecipeTypeViewSet(viewsets.ModelViewSet):
    queryset = RecipeType.objects.all().order_by('id')
    serializer_class = RecipeTypeSerializer

@require_http_methods(["GET", "POST"])
def recipe_list(request):
    recipes = Recipe.objects.all()
    recipes_data = [
        {
            'name': recipe.recipe_name,
            'description': recipe.recipe_description,
            'type': recipe.recipe_type.recipe_type_name
        }
        for recipe in recipes
    ]
    response = JsonResponse(
        {
            'recipes': recipes_data,
         },
        status=200,
        json_dumps_params={'indent': 4}
    )
    return response



@login_required(login_url='/')
@require_http_methods(["GET", "POST"])
def recipe_detail(request, *args, **kwargs):
    recipe_id = kwargs.get('recipe_id', None)

    if recipe_id is None:
        return JsonResponse(
            {
                'error': 'recipe_id must be provided',
            },
            status=400
        )

    recipe = Recipe.objects.get(pk=recipe_id)

    if recipe is not None:
        data = {
            'name': recipe.recipe_name,
            'description': recipe.recipe_description,
            'type': recipe.recipe_type.recipe_type_name
        }
        response_json = {
            'user': request.user.username,
            'data': data
        }
        response = JsonResponse(
            response_json,
            status=200
        )
    else:
        response = JsonResponse(
            {'error': f'recipe with id {recipe_id} not found'},
            status=404
        )
    return response


@require_http_methods(["GET", "POST"])
def recipe_category(request, *args, **kwargs):
    category_id = kwargs.get('category_id', None)
    response = JsonResponse(
        {
            'recipes': [],
            'category_id': category_id,
        },
        status=200
    )
    return response

