from django.db import models


class RecipeType(models.Model):
    RECIPE_TYPES = (
        ('C', 'Cocktail'),
        ('D', 'Dish'),
    )
    recipe_type_name = models.CharField(max_length=128, choices=RECIPE_TYPES, verbose_name='Recipe Type')


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=256, verbose_name='Recipe title')
    recipe_type = models.ForeignKey(RecipeType, on_delete=models.SET_NULL, null=True, verbose_name='Recipe Type')
    # recipe_image = models.ImageField()
    recipe_description = models.TextField(max_length=4000, verbose_name='Recipe Content')