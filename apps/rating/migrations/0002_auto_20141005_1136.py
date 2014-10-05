# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.rating.utils


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.PositiveSmallIntegerField(verbose_name='kind', choices=[(1, 'evil'), (2, 'easier'), (3, 'vague'), (4, 'brainy')])),
                ('image', models.ImageField(upload_to=apps.rating.utils.UploadTo(b'option'), verbose_name='image')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]
