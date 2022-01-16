from django.urls import path
from . import views

urlpatterns = [
    path('ru/', views.blog_ru, name='blog_ru'),
    path('az/', views.blog_az, name='blog_az'),
    path('ru/<int:id>/', views.single_blog_ru, name='single_blog_ru'),
    path('az/<int:id>/', views.single_blog_az, name='single_blog_az'),
    path('ru/search/', views.search_ru, name='search_ru'),
    path('az/search/', views.search_az, name='search_az'),
    
]