from django.contrib import admin
from django.urls import path
from . import views
...
urlpatterns = [
    path('luke_skywalker/', views.get_luke_data), 
    path('', views.get_people_list, name='people_list'),
    path('character/<int:id>', views.get_character_data, name='character')
]

