from django.db import models
from django.utils import timezone

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Film(models.Model):
    title = models.CharField(max_length = 255)

    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    created_in_country = models.ForeignKey(Country, on_delete = models.CASCADE, related_name = 'country')
    available_in_countries = models.ManyToManyField(Country, related_name = 'available_countries')

    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()

        self.modified = timezone.now()
        return super(Film, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

        