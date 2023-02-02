# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .managers import CustomerManager, ThemeManager, ThemeCustomerManager
from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True, null=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)

    objects = CustomerManager()


class Theme(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True, null=True)

    objects = ThemeManager()


class ThemeCustomer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.ForeignKey(Theme, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    objects = ThemeCustomerManager()
