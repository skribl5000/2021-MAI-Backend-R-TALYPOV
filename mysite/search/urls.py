from django.urls import path

from .views import SearchRecipes

urlpatterns = [
    path('recipes/<str:query>/', SearchRecipes.as_view()),
]