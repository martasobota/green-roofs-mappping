# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 08:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warsaw', '0004_auto_20170406_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greenroof',
            name='mpoly',
        ),
    ]
