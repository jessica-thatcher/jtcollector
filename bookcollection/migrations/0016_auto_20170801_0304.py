# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-01 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcollection', '0015_auto_20170725_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
