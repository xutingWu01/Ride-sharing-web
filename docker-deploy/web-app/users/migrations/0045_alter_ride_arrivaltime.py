# Generated by Django 4.0.1 on 2022-02-06 03:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0044_alter_ride_arrivaltime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='arrivaltime',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 3, 16, 45, 967181, tzinfo=utc)),
        ),
    ]
