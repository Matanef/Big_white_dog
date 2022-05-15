from socket import fromshare
from django import forms
from .models import Customer, Vehicle, Vehicle_Type, Vehicle_Size, Rental


class RentalForm (forms.Form):
    rental_date = forms.DateField(widget=forms.TextInput)
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all())

class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)

class VehicleForm(forms.Form):
    vehicle_type = forms.ModelChoiceField(queryset=Vehicle_Type.objects.all())
    real_cost = forms.IntegerField()
    size = forms.ModelChoiceField(queryset=Vehicle_Size.objects.all())