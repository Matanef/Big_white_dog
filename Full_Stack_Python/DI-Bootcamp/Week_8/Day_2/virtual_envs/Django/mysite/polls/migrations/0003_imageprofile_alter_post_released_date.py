# Generated by Django 4.0.4 on 2022-05-11 07:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProfile',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='polls.person')),
                ('image', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='released_date',
            field=models.DateField(default=datetime.datetime(2022, 5, 11, 7, 55, 15, 284377)),
        ),
    ]
