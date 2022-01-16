from django.contrib import admin
from django.utils.html import format_html
from recipes.models import Recipe

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 20px" />'.format(object.recipe_photo.url))

    thumbnail.short_description = 'Recipe Image'

    list_display = ('thumbnail', 'recipe_title_ru', 'is_featured', 'created_date')
    list_display_links = ('thumbnail', 'recipe_title_ru')
    list_editable = ('is_featured',)
    search_fields = ('recipe_title_ru',)

admin.site.register(Recipe, RecipeAdmin)
