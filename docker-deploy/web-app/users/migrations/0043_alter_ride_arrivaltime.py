# Generated by Django 4.0.1 on 2022-02-05 20:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_alter_ride_arrivaltime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='arrivaltime',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 20, 24, 18, 41744, tzinfo=utc)),
        ),
    ]
