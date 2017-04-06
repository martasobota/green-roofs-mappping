# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from warsaw.models import City, District


def populate(apps, schema_editor):
    warsaw = City.objects.create(name="Warsaw")
    District.objects.create(name="Wola", city=warsaw)
    District.objects.create(name="Śródmieście", city=warsaw)
    District.objects.create(name="Mokotów", city=warsaw)
    District.objects.create(name="Ursus", city=warsaw)
    District.objects.create(name="Bemowo", city=warsaw)
    District.objects.create(name="Wawer", city=warsaw)
    District.objects.create(name="Ochota", city=warsaw)
    District.objects.create(name="Włochy", city=warsaw)
    District.objects.create(name="Wesoła", city=warsaw)
    District.objects.create(name="Bielany", city=warsaw)
    District.objects.create(name="Ursynów", city=warsaw)
    District.objects.create(name="Wilanów", city=warsaw)
    District.objects.create(name="Żoliborz", city=warsaw)
    District.objects.create(name="Targówek", city=warsaw)
    District.objects.create(name="Białołęka", city=warsaw)
    District.objects.create(name="Rembertów", city=warsaw)
    District.objects.create(name="Praga Północ", city=warsaw)
    District.objects.create(name="Praga Południe", city=warsaw)


class Migration(migrations.Migration):

    dependencies = [
        ('warsaw', '0002_auto_20170405_1252'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
