
from django.urls import path
from .views import*

urlpatterns = [
    path("",home),
    path("home/",home),
]
# urlpatterns = [
#     # path('', views.home, name='home'),
#     path('admin/', ...),  # Your admin patterns
#     path('Restro_App/', ...),  # Your Restro_App patterns
# ]