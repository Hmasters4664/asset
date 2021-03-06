# Generated by Django 2.2.2 on 2019-08-02 12:30

import AMS.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMS', '0004_auto_20190630_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='asset_is_rejected',
            field=models.BooleanField(default=False, verbose_name='rejected'),
        ),
        migrations.AddField(
            model_name='asset',
            name='rejection_reason',
            field=models.CharField(blank=True, max_length=50, validators=[AMS.validators.validate_characters]),
        ),
        migrations.AlterField(
            model_name='asset',
            name='current_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, validators=[AMS.validators.check_negative_number]),
        ),
    ]
