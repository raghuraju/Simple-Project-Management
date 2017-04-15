# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170414_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField()),
                ('joined_on', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=256)),
                ('employed_since', models.DateField()),
                ('designation', models.IntegerField(choices=[(0, 'PROJECT'), (1, 'SENIOR'), (2, 'EXECUTIVE')])),
                ('reports_to', models.ForeignKey(blank=True, to='users.ProjectManager', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='manager',
            name='reports_to',
        ),
        migrations.AlterField(
            model_name='team',
            name='incharge',
            field=models.ForeignKey(to='users.ProjectManager'),
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
