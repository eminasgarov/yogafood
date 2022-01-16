from ckeditor.fields import RichTextField
from django.db import models
from datetime import datetime

# Create your models here.


class Team(models.Model):
    first_name_ru       = models.CharField(max_length=50)
    first_name_az       = models.CharField(max_length=50)
    first_name_en       = models.CharField(max_length=50, blank=True)
    last_name_ru        = models.CharField(max_length=50)
    last_name_az        = models.CharField(max_length=50)
    last_name_en        = models.CharField(max_length=50, blank=True)
    designation_ru      = models.CharField(max_length=100)
    designation_az      = models.CharField(max_length=100)
    designation_en      = models.CharField(max_length=100, blank=True)
    about_ru            = RichTextField()
    about_az            = RichTextField()
    about_en            = RichTextField(blank=True)
    photo               = models.ImageField(upload_to='team/%Y/%m/%d/')
    created_date        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name_ru
    
    
class Email(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    created_date = models.DateField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email