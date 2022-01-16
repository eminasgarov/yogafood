# Generated by Django 4.0.1 on 2022-01-11 19:07

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_title_ru', models.CharField(max_length=100, unique=True)),
                ('recipe_title_az', models.CharField(max_length=100, unique=True)),
                ('recipe_description_ru', ckeditor.fields.RichTextField()),
                ('recipe_description_az', ckeditor.fields.RichTextField()),
                ('recipe_photo', models.ImageField(upload_to='recipes/%Y/%m/%d/')),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]