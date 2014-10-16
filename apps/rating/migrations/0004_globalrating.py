# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.rating.validators


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_remove_teacher_average_record'),
        ('rating', '0003_auto_20141016_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_evil_value', models.SmallIntegerField(verbose_name='evil value', validators=[apps.rating.validators.validate_rating_value])),
                ('total_easier_value', models.SmallIntegerField(verbose_name='easier value', validators=[apps.rating.validators.validate_rating_value])),
                ('total_vague_value', models.SmallIntegerField(verbose_name='vague value', validators=[apps.rating.validators.validate_rating_value])),
                ('total_brainy_value', models.SmallIntegerField(verbose_name='brainy value', validators=[apps.rating.validators.validate_rating_value])),
                ('average_record', models.DecimalField(default=0, verbose_name='average record', max_digits=5, decimal_places=3)),
                ('teacher', models.OneToOneField(related_name=b'global_rating', to='people.Teacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
