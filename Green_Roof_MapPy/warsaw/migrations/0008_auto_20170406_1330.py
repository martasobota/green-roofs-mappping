# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 13:30
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warsaw', '0007_auto_20170406_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greenroof',
            name='poly',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, max_length=2500, srid=4326),
        ),
    ]
