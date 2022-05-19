from django.contrib import admin
from .models import Person, Post, ImageProfile, Category

# Register your models here.
admin.site.register(Person)
admin.site.register(Post)
admin.site.register(ImageProfile)
admin.site.register(Category)