from django.contrib import admin

# Register your models here.

from .models import Customer
from .models import Vehicle_Type
from .models import Vehicle_Size
from .models import Vehicle
from .models import Rental
from .models import Rental_rate

admin.site.register(Customer)
admin.site.register(Vehicle_Type)
admin.site.register(Vehicle_Size)
admin.site.register(Vehicle)
admin.site.register(Rental)
admin.site.register(Rental_rate)
