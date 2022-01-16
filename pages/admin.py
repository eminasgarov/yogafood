from django.contrib import admin
from django.utils.html import format_html
from pages.models import Team, Email

# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 20px" />'.format(object.photo.url))

    thumbnail.short_description = 'Member Photo'

    list_display = ('thumbnail', 'first_name_ru', 'last_name_ru', 'designation_ru', 'created_date')
    list_display_links = ('thumbnail',)
    search_fields = ('first_name_ru', 'last_name_ru', 'designation_ru')

admin.site.register(Team, TeamAdmin)

class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'subject')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'email', 'subject')
    list_per_page = 25

admin.site.register(Email, EmailAdmin)