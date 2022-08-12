from rest_framework import serializers
from .models import Recipe, RecipeType


class RecipeSerializer(serializers.ModelSerializer):
    recipe_name = serializers.CharField(max_length=256)

    def validate_recipe_name(self, value):
        if value is None:
            raise serializers.ValidationError("Название должно быть не пустое.")
        recipe_data = Recipe.objects.get(recipe_name=value)
        if recipe_data is not None:
            raise serializers.ValidationError(f"Рецепт с назаванием '{value}' уже существует")
        return value

    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeTypeSerializer(serializers.ModelSerializer):
    recipe_type_name = serializers.CharField(max_length=128)

    def validate_recipe_type_name(self, value):
        if value is None:
            raise serializers.ValidationError("Название должно быть не пустое.")
        recipe_data = RecipeType.objects.get(recipe_type_name=value)
        if recipe_data is not None:
            raise serializers.ValidationError(f"Тип рецепта с назаванием '{value}' уже существует")
        return value

    class Meta:
        model = RecipeType
        fields = '__all__'
