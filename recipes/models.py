from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Recipe(models.Model):
    recipe_title_ru         = models.CharField(max_length=100, unique=True)
    recipe_title_az         = models.CharField(max_length=100, unique=True)
    recipe_title_en         = models.CharField(max_length=100, blank=True)
    recipe_brief_ru         = models.CharField(max_length=200, unique=True, blank=True)
    recipe_brief_az         = models.CharField(max_length=200, unique=True, blank=True)
    recipe_brief_en         = models.CharField(max_length=200, blank=True)
    recipe_description_ru   = RichTextField()
    recipe_description_az   = RichTextField()
    recipe_description_en   = RichTextField(blank=True)
    recipe_photo            = models.ImageField(upload_to='recipes/%Y/%m/%d/')
    recipe_photo_1          = models.ImageField(upload_to='recipes/%Y/%m/%d/', blank=True)
    recipe_photo_2          = models.ImageField(upload_to='recipes/%Y/%m/%d/', blank=True)
    recipe_photo_3          = models.ImageField(upload_to='recipes/%Y/%m/%d/', blank=True)
    recipe_photo_4          = models.ImageField(upload_to='recipes/%Y/%m/%d/', blank=True)
    recipe_photo_5          = models.ImageField(upload_to='recipes/%Y/%m/%d/', blank=True)
    is_featured             = models.BooleanField(default=False)
    created_date            = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.recipe_title_ru