# Generated by Django 4.0.1 on 2022-01-12 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_rename_ricipe_brief_az_recipe_recipe_brief_az_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_photo_2',
            field=models.ImageField(blank=True, upload_to='recipes/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_photo_5',
            field=models.ImageField(blank=True, upload_to='recipes/%Y/%m/%d/'),
        ),
    ]