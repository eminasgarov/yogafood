from django.urls import path
from . import views

urlpatterns = [
    path('ru/', views.recipe_ru, name='recipe_ru'),
    path('az/', views.recipe_az, name='recipe_az'),
    path('ru/<int:id>/', views.single_recipe_ru, name='single_recipe_ru'),
    path('az/<int:id>/', views.single_recipe_az, name='single_recipe_az'),
    path('ru/search/', views.search_ru, name='search_ru'),
    path('az/search/', views.search_az, name='search_az'),
    
]