# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-02-02 14:22
from __future__ import unicode_literals

from django.db import migrations
import sender.managers


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0004_auto_20230202_1345'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='themecustomer',
            managers=[
                ('objects', sender.managers.ThemeCustomerManager()),
            ],
        ),
    ]