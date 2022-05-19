from django.contrib import admin
from .models import Animal, Family
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Animal)
admin.site.register(Family)
admin.site.register(User)
