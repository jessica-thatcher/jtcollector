# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-20 13:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookcollection', '0009_auto_20170719_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subgenre',
            name='genre',
        ),
    ]
