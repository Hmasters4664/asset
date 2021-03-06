# Generated by Django 2.2.2 on 2019-06-22 11:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('building', models.TextField(blank=True, max_length=1000)),
                ('floor', models.CharField(max_length=3)),
                ('adress', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset_id', models.AutoField(primary_key=True, serialize=False)),
                ('acquisition_date', models.DateField(default=datetime.date.today)),
                ('asset_name', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(max_length=2000)),
                ('asset_type', models.CharField(choices=[('Automobile', 'Automobile'), ('AV Equipment', 'AV Equipment'), ('Computer Equipment', 'Computer Equipment'), ('Office Furniture & Stationary', 'Office Furniture & Stationary')], max_length=30)),
                ('asset_barcode', models.CharField(blank=True, max_length=30)),
                ('asset_serial_number', models.CharField(blank=True, max_length=80)),
                ('asset_status', models.CharField(choices=[('Working', 'Working'), ('Disabled', 'Disabled')], max_length=10)),
                ('asset_user', models.CharField(blank=True, max_length=30)),
                ('added_date', models.DateField(default=datetime.date.today)),
                ('modified_date', models.DateField(default=datetime.date.today)),
                ('purchase_value', models.DecimalField(decimal_places=2, default=200.0, max_digits=19)),
                ('residual_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('current_value', models.DecimalField(decimal_places=2, max_digits=19)),
                ('life_expectancy', models.IntegerField(default=3)),
                ('depr_model', models.CharField(choices=[('Straight Line', 'Straight Line'), ('Double-Declining Balance', 'Double-Declining Balance'), ('Sum of Years', 'Sum of Years')], default='Straight Line', max_length=30)),
                ('currentVal_date', models.DateField(default=datetime.date.today)),
                ('asset_is_approved', models.BooleanField(default=False, verbose_name='approved')),
                ('asset_department', models.CharField(choices=[('I.T', 'I.T'), ('Finance', 'Finance'), ('Marketing', 'Marketing'), ('Sales', 'Sales')], max_length=10)),
                ('asset_location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AMS.Location')),
                ('asset_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
