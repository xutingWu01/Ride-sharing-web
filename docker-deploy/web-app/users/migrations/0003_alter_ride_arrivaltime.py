# Generated by Django 4.0.1 on 2022-01-30 21:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_ride_arrivaltime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='arrivaltime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 30, 21, 25, 26, 444514, tzinfo=utc)),
        ),
    ]
