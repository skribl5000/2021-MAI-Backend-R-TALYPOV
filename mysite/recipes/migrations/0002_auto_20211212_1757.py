# Generated by Django 3.0 on 2021-12-12 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_description',
            field=models.TextField(max_length=4000, verbose_name='Recipe Content'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_name',
            field=models.CharField(max_length=256, verbose_name='Recipe title'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.RecipeType', verbose_name='Recipe Type'),
        ),
        migrations.AlterField(
            model_name='recipetype',
            name='recipe_type_name',
            field=models.CharField(choices=[('C', 'Cocktail'), ('D', 'Dish')], max_length=128, verbose_name='Recipe Type'),
        ),
    ]
