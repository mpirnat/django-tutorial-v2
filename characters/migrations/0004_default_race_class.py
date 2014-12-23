# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from characters.models import Race, Class


def load_data(apps, schema_editor):
    Race(name="Human", description="Enh.").save()
    Class(name="Generic", description="Meh.").save()


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_class_race'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
