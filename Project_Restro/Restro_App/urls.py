
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.home, name = 'home'),
    path('home/',views.home, name = 'home'),
    path('about/', views.aboutUs, name='about'),
    path('booking/', views.booking, name = 'booking'),
    path('contact/', views.contact, name = 'contact'),
    path('menu/', views.Menu, name = 'menu'),
    path('service/', views.Service, name = 'service'),
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns = [
#     # path('', views.home, name='home'),
#     path('admin/', ...),  # Your admin patterns
#     path('Restro_App/', ...),  # Your Restro_App patterns
# ]