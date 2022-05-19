from ast import For
from django.db import models
from django.db.models import Model



class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Vehicle_Type(models.Model):
     name = models.CharField(max_length=100)

def __str__(self):
    return self.name


class Vehicle_Size(models.Model):
     name = models.CharField(max_length=100)

def __str__(self):
    return self.name


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.IntegerField(blank=False)
    size = models.ForeignKey(Vehicle_Size, on_delete=models.CASCADE)

class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class Rental_rate(models.Model):
    daily_rate = models.IntegerField()
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(Vehicle_Size, on_delete=models.CASCADE)
