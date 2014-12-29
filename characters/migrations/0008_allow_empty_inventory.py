# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0007_item_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='inventory',
            field=models.ManyToManyField(to='characters.Item', blank=True, null=True),
            preserve_default=True,
        ),
    ]
