# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0005_auto_20141017_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalrating',
            name='average_record',
            field=models.DecimalField(default=0, verbose_name='average record', max_digits=5, decimal_places=3, validators=django.core.validators.MinValueValidator(0)),
        ),
        migrations.AlterField(
            model_name='globalrating',
            name='total_brainy_value',
            field=models.IntegerField(default=0, verbose_name='total brainy value', validators=django.core.validators.MinValueValidator(0)),
        ),
        migrations.AlterField(
            model_name='globalrating',
            name='total_easier_value',
            field=models.IntegerField(default=0, verbose_name='total easier value', validators=django.core.validators.MinValueValidator(0)),
        ),
        migrations.AlterField(
            model_name='globalrating',
            name='total_evil_value',
            field=models.IntegerField(default=0, verbose_name='total evil value', validators=django.core.validators.MinValueValidator(0)),
        ),
        migrations.AlterField(
            model_name='globalrating',
            name='total_vague_value',
            field=models.IntegerField(default=0, verbose_name='total vague value', validators=django.core.validators.MinValueValidator(0)),
        ),
    ]
