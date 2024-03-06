from django.db import models
from django.utils import timezone


# Create your models here.


class Table(models.Model):
    # table = models.ForeignKey(BookTable, on_delete=models.CASCADE)
    table_no = models.CharField(max_length=5)
    price = models.IntegerField(null=True, blank =True)
    
    def __str__(self):
        return self.table_no

class Reservation(models.Model):
    name = models.CharField( max_length=20, null = False)
    email = models.EmailField(max_length = 30, null = True, blank = True)
    datetime = models.DateTimeField()
    people = models.IntegerField()
    number = models.CharField(max_length=14)
    table = models.ForeignKey(Table, on_delete= models.CASCADE)
    special_request =models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
# class TablePrice(models.Model):
#     table = models.ForeignKey(BookTable, on_delete=models.CASCADE)
#     price = models.IntegerField(null=True, blank =True)
    
#     def __str__(self):
#         return str(self.table.table_no)

class Category(models.Model):
    name =models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    

class FoodMenu(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length=30, null =True, blank=True)
    description = models.TextField(null=True, blank=True) 
    image = models.ImageField(upload_to='uploads/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
        return self.name
        
    
    
    