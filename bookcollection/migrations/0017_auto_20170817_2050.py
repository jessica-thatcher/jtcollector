# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-17 20:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookcollection', '0016_auto_20170801_0304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
    ]
