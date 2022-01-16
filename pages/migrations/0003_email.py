# Generated by Django 4.0.1 on 2022-01-15 16:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_team_about_en_team_designation_en_team_first_name_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('created_date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]