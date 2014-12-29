# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_fk_race_class'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'Classes'},
        ),
        migrations.AlterField(
            model_name='character',
            name='cclass',
            field=models.ForeignKey(verbose_name='class', to='characters.Class'),
            preserve_default=True,
        ),
    ]
