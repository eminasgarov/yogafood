from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    blog_title_ru         = models.CharField(max_length=100, unique=True)
    blog_title_az         = models.CharField(max_length=100, unique=True)
    blog_title_en         = models.CharField(max_length=100, blank=True)
    blog_brief_ru         = models.CharField(max_length=200, unique=True, blank=True)
    blog_brief_az         = models.CharField(max_length=200, unique=True, blank=True)
    blog_brief_en         = models.CharField(max_length=200, blank=True)
    blog_description_ru   = RichTextField()
    blog_description_az   = RichTextField()
    blog_description_en   = RichTextField(blank=True)
    blog_photo            = models.ImageField(upload_to='recipes/%Y/%m/%d/')
    blog_photo_1          = models.ImageField(upload_to='recipes/%Y/%m/%d/', blank=True)
    blog_photo_2          = models.ImageField(upload_to='recipes/%Y/%m/%d/', blank=True)
    blog_photo_3          = models.ImageField(upload_to='recipes/%Y/%m/%d/', blank=True)
    blog_photo_4          = models.ImageField(upload_to='recipes/%Y/%m/%d/', blank=True)
    blog_photo_5          = models.ImageField(upload_to='recipes/%Y/%m/%d/', blank=True)
    is_featured           = models.BooleanField(default=False)
    created_date          = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.blog_title_ru