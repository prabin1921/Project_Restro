from django.db import models


# Create your models here.
class BookTable(models.Model):
    Name = models.CharField( max_length=20)
    Email = models.EmailField(max_length = 30)
    DateTime = models.DateTimeField(auto_now=True)
    No_People = models.IntegerField()
    SpecialRequest=models.TextField()
    Ph_Number = models.CharField(max_length=14)
    
    def __str__(self):
        return self.name
    
    