# Generated by Django 4.1 on 2022-08-11 01:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0073_alter_ride_arrivaltime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='arrivaltime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 11, 1, 51, 41, 320803, tzinfo=datetime.timezone.utc)),
        ),
    ]
