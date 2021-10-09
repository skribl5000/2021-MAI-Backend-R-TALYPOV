from django.db import models


class RecipeType(models.Model):
    RECIPE_TYPES = (
        ('C', 'Cocktail'),
        ('D', 'Dish'),
    )
    recipe_type_name = models.CharField(max_length=128, choices=RECIPE_TYPES)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=256)
    recipe_type = models.ForeignKey(RecipeType, on_delete=models.SET_NULL, null=True)
    # recipe_image = models.ImageField()
    recipe_description = models.TextField(max_length=4000)

