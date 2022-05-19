from django.db import models


# Create your models here.

class Animal(models.Model):
    animalid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    legs = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    speed = models.IntegerField()
    family = models.IntegerField()

class Family(models.Model):
    familyid = models.IntegerField()
    name = models.CharField(max_length=100)



