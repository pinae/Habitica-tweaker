# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync_accounts', '0003_auto_20160822_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyhistory',
            name='date',
            field=models.BigIntegerField(default=0),
        ),
    ]