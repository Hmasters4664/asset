# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
import datetime
from django.conf import settings
from .managers import UserManager
from django.utils.translation import ugettext_lazy as _
from .validators import validate_characters, check_negative_number, check_zero_number
# Create your models here.


class Asset(models.Model):
    
    ASSET_CHOICES = (
            ('Automobile',   'Automobile'),
            ('AV Equipment', 'AV Equipment'),
            ('Computer Equipment',  'Computer Equipment'),
            ('Office Furniture & Stationary', 'Office Furniture & Stationary'),
        )

    DEPARTMENT = (
        ('I.T', 'I.T'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
        ('Sales', 'Sales'),
    )
    STATUS_CHOICES = (
            ('Working', 'Working'),
            ('Disabled', 'Disabled'),
    )

    Depreciation = (
        ('Straight Line', 'Straight Line'),
        ('Double-Declining Balance', 'Double-Declining Balance'),
        ('Sum of Years', 'Sum of Years'),
    )
    asset_id = models.AutoField(primary_key=True)
    acquisition_date = models.DateField(default=datetime.date.today)
    asset_name = models.CharField(max_length=50, blank=True, validators=[validate_characters], )
    description = models.TextField(max_length=200, validators=[validate_characters],)
    asset_type = models.CharField(choices=ASSET_CHOICES, max_length=30, validators=[validate_characters],)
    asset_barcode = models.CharField(max_length=30, blank=True,validators=[validate_characters], )
    asset_serial_number = models.CharField(max_length=80, blank=True, validators=[validate_characters], )
    asset_location = models.ForeignKey("Location", on_delete=models.PROTECT, blank=True, null=True)
    asset_status = models.CharField(choices=STATUS_CHOICES, max_length=10, validators=[validate_characters],)
    asset_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    asset_user = models.CharField(max_length=30, blank=True, validators=[validate_characters], )
    added_date = models.DateField(default=datetime.date.today)
    modified_date = models.DateField(default=datetime.date.today)
    purchase_value = models.DecimalField(max_digits=19, decimal_places=2,default=200.00,validators = [check_negative_number, check_zero_number],)
    residual_value = models.DecimalField(max_digits=19, decimal_places=2,default=0.00,validators = [check_negative_number])
    current_value = models.DecimalField(max_digits=19, decimal_places=2,validators = [check_negative_number],blank=True)
    life_expectancy = models.IntegerField(default=3,validators = [check_negative_number, check_zero_number])
    depr_model = models.CharField(choices=Depreciation, max_length=30,default='Straight Line', validators=[validate_characters],)
    currentVal_date = models.DateField(default=datetime.date.today)
    asset_is_approved = models.BooleanField(_('approved'), default=False)
    asset_is_rejected = models.BooleanField(_('rejected'), default=False)
    rejection_reason = models.CharField(max_length=50, blank=True, validators=[validate_characters], )
    asset_department = models.CharField(choices=DEPARTMENT, max_length=10,validators=[validate_characters],)

    def natural_key(self):
        return self.my_natural_key

    def save(self, *args, **kwargs):
        if not self.current_value:
            self.current_value = self.purchase_value

        if self.residual_value > self.purchase_value:
            self.residual_value = 0.00

        if self.asset_is_rejected:
            self.asset_is_approved = False

        if self.asset_is_approved:
            self.asset_is_rejected = False
            self.rejection_reason = ''

        super().save(*args, **kwargs)


class Location(models.Model):
    location_id= models.AutoField(primary_key=True)
    city = models.CharField(max_length=50,validators=[validate_characters],)
    province = models.CharField(max_length=50,validators=[validate_characters],)
    country = models.CharField(max_length=20,validators=[validate_characters],)
    building = models.TextField(max_length=1000, blank=True,validators=[validate_characters],)
    floor = models.CharField(max_length=3,validators=[validate_characters],)
    adress = models.TextField(max_length=200,validators=[validate_characters],)

    def __str__(self):
        return self.adress

    def natural_key(self):
        return self.my_natural_key


class Records(models.Model):
    description = models.TextField(max_length=1000)
    date = models.DateField(default=datetime.date.today)

    def natural_key(self):
        return self.my_natural_key




