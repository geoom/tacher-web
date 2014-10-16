# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.rating.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0002_auto_20141004_1033'),
        ('rating', '0002_auto_20141005_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evil_value', models.SmallIntegerField(verbose_name='evil value', validators=[apps.rating.validators.validate_rating_value])),
                ('easier_value', models.SmallIntegerField(verbose_name='easier value', validators=[apps.rating.validators.validate_rating_value])),
                ('vague_value', models.SmallIntegerField(verbose_name='vague value', validators=[apps.rating.validators.validate_rating_value])),
                ('brainy_value', models.SmallIntegerField(verbose_name='brainy value', validators=[apps.rating.validators.validate_rating_value])),
                ('teacher', models.ForeignKey(related_name=b'ratings', to='people.Teacher')),
                ('user', models.ForeignKey(related_name=b'ratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='ratingoption',
            options={'verbose_name': 'rating option', 'verbose_name_plural': 'rating options'},
        ),
    ]
