from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length= 50, blank=True, null=True)
    email = models.CharField(max_length= 50,blank=True, null=True)
    phone = models.CharField(max_length= 50,blank=True, null=True)
    date = models.DateField(max_length= 50, blank=True, null=True)
    def __str__(self):
        return self.name