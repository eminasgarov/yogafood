# Generated by Django 4.0.1 on 2022-01-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_recipe_brief_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_title_en',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ricipe_brief_en',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
