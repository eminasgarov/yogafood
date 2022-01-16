from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ru/', views.home_ru, name='home_ru'),
    path('az/', views.home_az, name='home_az'),
    path('ru/about', views.about_ru, name='about_ru'),
    path('az/about', views.about_az, name='about_az'),
    path('ru/contact', views.contact_ru, name='contact_ru'),
    path('az/contact', views.contact_az, name='contact_az'),
]