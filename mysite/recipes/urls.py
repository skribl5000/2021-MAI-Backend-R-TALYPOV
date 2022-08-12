from .views import recipe_list, recipe_detail, recipe_category

from django.urls import path, re_path
urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('category/<int:category_id>/', recipe_category, name='recipe_category'),
    path('<int:recipe_id>/', recipe_detail, name='recipe_detail')
]
