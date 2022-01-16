# Generated by Django 4.0.1 on 2022-01-11 19:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_description_en',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_title_en',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]