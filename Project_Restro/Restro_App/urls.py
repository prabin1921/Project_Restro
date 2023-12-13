
# from django.contrib import admin
from django.urls import path
from . import views
from .views import home

urlpatterns = [
    # path("app/", ...),
    path("",home),
    path("/app/home/",home),
]
# urlpatterns = [
#     # path('', views.home, name='home'),
#     path('admin/', ...),  # Your admin patterns
#     path('Restro_App/', ...),  # Your Restro_App patterns
# ]