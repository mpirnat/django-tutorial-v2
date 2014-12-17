# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import characters.models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='alignment',
            field=models.CharField(choices=[('LG', 'Lawful Good'), ('LN', 'Lawful Neutral'), ('LE', 'Lawful Evil'), ('NG', 'Neutral Good'), ('NN', 'Netural'), ('NE', 'Neutral Evil'), ('CG', 'Chaotic Good'), ('CN', 'Chaotic Neutral'), ('CE', 'Chaotic Evil')], max_length=2, default='NN'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='charisma',
            field=models.IntegerField(default=characters.models.generate_stat),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='constitution',
            field=models.IntegerField(default=characters.models.generate_stat),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='current_hit_points',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='dexterity',
            field=models.IntegerField(default=characters.models.generate_stat),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='experience_points',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(default=characters.models.generate_stat),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='level',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='max_hit_points',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='strength',
            field=models.IntegerField(default=characters.models.generate_stat),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='wisdom',
            field=models.IntegerField(default=characters.models.generate_stat),
            preserve_default=True,
        ),
    ]
