# Generated by Django 3.0.1 on 2019-12-25 08:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0002_film_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]