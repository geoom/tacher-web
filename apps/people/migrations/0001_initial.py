# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('average_record', models.DecimalField(default=0, max_digits=5, decimal_places=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
