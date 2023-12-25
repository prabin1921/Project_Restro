
# from django.contrib import admin
from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path(" ",home),
    path("home/", views.home, name = "home"),
    
]
# urlpatterns = [
#     # path('', views.home, name='home'),
#     path('admin/', ...),  # Your admin patterns
#     path('Restro_App/', ...),  # Your Restro_App patterns
# ]