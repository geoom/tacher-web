# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ('name',), 'verbose_name': 'teacher', 'verbose_name_plural': 'teachers'},
        ),
        migrations.AddField(
            model_name='teacher',
            name='avatar_url',
            field=models.URLField(null=True, verbose_name='avatar url', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='average_record',
            field=models.DecimalField(default=0, verbose_name='average record', max_digits=5, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='description',
            field=models.TextField(verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=15, verbose_name='name'),
        ),
    ]
