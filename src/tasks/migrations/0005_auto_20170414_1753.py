# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20170414_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Started'), (2, 'Finished'), (3, 'Testing'), (4, 'Released')], default='Pending', max_length=1),
        ),
    ]
