
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
    path('checkout/', views.CheckOut, name = 'checkout'),
    
    path('get_table_price/<int:table_id>/', views.get_table_price, name='get_table_price')
       
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
