from django.contrib import admin
from .models import*
from .views import*

# Register your models here.
admin.site.register(Reservation)
admin.site.register(FoodMenu)
admin.site.register(Category)
admin.site.register(Table)