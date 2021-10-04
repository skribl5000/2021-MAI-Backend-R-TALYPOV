from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def recipe_list(request):
    response = JsonResponse(
        {
            'recipes': [],
         },
        status=200
    )
    return response


@require_http_methods(["GET", "POST"])
def recipe_detail(request, *args, **kwargs):
    recipe_id = kwargs.get('recipe_id', None)
    if recipe_id is not None:
        response = JsonResponse(
            {
                'details': f'Details of {recipe_id} recipe',
            },
            status=200
        )
    else:
        response = JsonResponse(
            {
                'error': 'recipe_id must be provided',
            },
            status=400
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

