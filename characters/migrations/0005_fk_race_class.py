# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_default_race_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='cclass',
            field=models.ForeignKey(default=1, to='characters.Class'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.ForeignKey(default=1, to='characters.Race'),
            preserve_default=False,
        ),
    ]
