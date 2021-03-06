# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20170416_0549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gender',
            options={'verbose_name_plural': 'Gender'},
        ),
        migrations.AlterModelOptions(
            name='managerdesignation',
            options={'verbose_name': 'Designation', 'verbose_name_plural': 'Designations'},
        ),
        migrations.AlterModelOptions(
            name='projectmanager',
            options={'verbose_name': 'Manager', 'verbose_name_plural': 'Managers'},
        ),
        migrations.AlterField(
            model_name='projectmanager',
            name='reports_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Executive'),
        ),
    ]
