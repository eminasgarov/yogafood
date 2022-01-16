# Generated by Django 4.0.1 on 2022-01-11 19:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='about_en',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='team',
            name='designation_en',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='team',
            name='first_name_en',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='team',
            name='last_name_en',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
