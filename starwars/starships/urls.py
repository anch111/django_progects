from django.urls import path, include
from . import views

urlpatterns = [
    path('xwing/', views.get_xwing_info),
    path('imperial_shuttle/', views.get_imperial_shuttle_info),
]

