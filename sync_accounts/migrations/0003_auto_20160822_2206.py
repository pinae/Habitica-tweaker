# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync_accounts', '0002_auto_20160819_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='repeat_days',
            field=models.CharField(blank=True, max_length=90),
        ),
    ]
