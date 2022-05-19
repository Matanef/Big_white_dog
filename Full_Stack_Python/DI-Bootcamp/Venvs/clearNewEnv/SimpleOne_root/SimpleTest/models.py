from pyexpat import model
from django.db import models

# Create your models here.

class SimplePerson(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    has_pet = models.BooleanField(default=True)
    number_pet = models.IntegerField()
