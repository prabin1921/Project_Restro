
from django.urls import path
from .import views


urlpatterns = [
    path("",views.home, name = 'home'),
    path('home/',views.home, name = 'home'),
    path('about/', views.aboutUs, name='about'),
    path('booking/', views.booking, name = 'booking'),
    path('contact/', views.contact, name = 'contact'),
    path('menu/', views.Menu, name = 'menu'),
    path('service/', views.Service, name = 'service'),
    
    
]
# urlpatterns = [
#     # path('', views.home, name='home'),
#     path('admin/', ...),  # Your admin patterns
#     path('Restro_App/', ...),  # Your Restro_App patterns
# ]