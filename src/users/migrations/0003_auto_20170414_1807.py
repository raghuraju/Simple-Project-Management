# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170414_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='reports_to',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Manager'),
        ),
    ]