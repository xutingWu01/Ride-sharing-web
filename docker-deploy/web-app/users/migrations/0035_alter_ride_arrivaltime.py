# Generated by Django 4.0.1 on 2022-01-31 21:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_alter_ride_arrivaltime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='arrivaltime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 31, 21, 45, 7, 838797, tzinfo=utc)),
        ),
    ]
