# Generated by Django 4.0.1 on 2022-01-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_recipe_description_en_recipe_recipe_title_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_brief_ru',
            field=models.CharField(blank=True, max_length=80, unique=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ricipe_brief_az',
            field=models.CharField(blank=True, max_length=80, unique=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ricipe_brief_en',
            field=models.CharField(blank=True, max_length=80, unique=True),
        ),
    ]
