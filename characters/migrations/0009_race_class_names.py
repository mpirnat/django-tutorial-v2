# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0008_allow_empty_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=200, verbose_name='class'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(max_length=200, verbose_name='race'),
            preserve_default=True,
        ),
    ]
