from django.shortcuts import render, get_list_or_404
from .models import *
from .forms import RentalForm, CustomerForm, VehicleForm
from datetime import date

# Create your views here.

def all_rental(request):
    rental_unreturned = Rental.objects.filter(return_date=None)
    rental_returned = Rental.objects.filter(return_date__isnull = False)
    return render(request, 'rental.html', {'unreturned':rental_unreturned, 'returned':rental_returned})




