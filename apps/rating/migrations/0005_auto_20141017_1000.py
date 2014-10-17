# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0004_globalrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalrating',
            name='total_brainy_value',
            field=models.IntegerField(verbose_name='total brainy value'),
        ),
        migrations.AlterField(
            model_name='globalrating',
            name='total_easier_value',
            field=models.IntegerField(verbose_name='total easier value'),
        ),
        migrations.AlterField(
            model_name='globalrating',
            name='total_evil_value',
            field=models.IntegerField(verbose_name='total evil value'),
        ),
        migrations.AlterField(
            model_name='globalrating',
            name='total_vague_value',
            field=models.IntegerField(verbose_name='total vague value'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(related_name=b'ratings', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
