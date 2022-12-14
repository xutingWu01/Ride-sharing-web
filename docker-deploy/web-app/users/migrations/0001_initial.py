# Generated by Django 4.0.1 on 2022-01-30 21:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.EmailField(max_length=254, null=True)),
                ('vehicle_type', models.CharField(default='Sedan', max_length=10)),
                ('plate_number', models.CharField(default='test', max_length=10)),
                ('max_passanger', models.CharField(default='4', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='haha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=100)),
                ('status_flag', models.CharField(max_length=1)),
                ('vehicle_id', models.CharField(max_length=10, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=30)),
                ('arrivaltime', models.DateTimeField(default=datetime.datetime(2022, 1, 30, 21, 25, 6, 790242, tzinfo=utc))),
                ('NumPassanger', models.IntegerField()),
                ('CanShare', models.IntegerField()),
                ('owner_id', models.IntegerField(null=True)),
                ('max_passanger', models.IntegerField(null=True)),
                ('status', models.IntegerField(default=0)),
                ('owner_email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_owner_email', models.EmailField(max_length=254, null=True)),
                ('r_driver_email', models.EmailField(max_length=254, null=True)),
                ('r_sharer_email', models.EmailField(max_length=254, null=True)),
                ('r_request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ride')),
            ],
        ),
    ]
