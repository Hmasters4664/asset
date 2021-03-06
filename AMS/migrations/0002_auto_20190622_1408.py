# Generated by Django 2.2.2 on 2019-06-22 14:08

import AMS.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_barcode',
            field=models.CharField(blank=True, max_length=30, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_department',
            field=models.CharField(choices=[('I.T', 'I.T'), ('Finance', 'Finance'), ('Marketing', 'Marketing'), ('Sales', 'Sales')], max_length=10, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_name',
            field=models.CharField(blank=True, max_length=50, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_serial_number',
            field=models.CharField(blank=True, max_length=80, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_status',
            field=models.CharField(choices=[('Working', 'Working'), ('Disabled', 'Disabled')], max_length=10, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.CharField(choices=[('Automobile', 'Automobile'), ('AV Equipment', 'AV Equipment'), ('Computer Equipment', 'Computer Equipment'), ('Office Furniture & Stationary', 'Office Furniture & Stationary')], max_length=30, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_user',
            field=models.CharField(blank=True, max_length=30, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='asset',
            name='depr_model',
            field=models.CharField(choices=[('Straight Line', 'Straight Line'), ('Double-Declining Balance', 'Double-Declining Balance'), ('Sum of Years', 'Sum of Years')], default='Straight Line', max_length=30, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='asset',
            name='description',
            field=models.TextField(max_length=2000, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='location',
            name='adress',
            field=models.TextField(max_length=200, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='location',
            name='building',
            field=models.TextField(blank=True, max_length=1000, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=50, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=20, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='location',
            name='province',
            field=models.CharField(max_length=50, validators=[AMS.validators.validate_characters]),
        ),
    ]
