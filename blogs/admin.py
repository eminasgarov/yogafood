from django.contrib import admin
from django.utils.html import format_html
from blogs.models import Blog


# Register your models here.

class BlogAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 20px" />'.format(object.blog_photo.url))

    thumbnail.short_description = 'Blog Image'

    list_display = ('thumbnail', 'blog_title_ru', 'is_featured', 'created_date')
    list_display_links = ('thumbnail', 'blog_title_ru')
    list_editable = ('is_featured',)
    search_fields = ('blog_title_ru',)

admin.site.register(Blog, BlogAdmin)