# Generated by Django 4.1 on 2022-08-12 01:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0076_alter_ride_arrivaltime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='arrivaltime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 12, 1, 40, 9, 475198, tzinfo=datetime.timezone.utc)),
        ),
    ]
