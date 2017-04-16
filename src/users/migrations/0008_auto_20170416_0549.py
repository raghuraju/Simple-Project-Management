# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 05:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170415_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerDesignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='designer',
            name='active',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='active',
        ),
        migrations.RemoveField(
            model_name='executive',
            name='active',
        ),
        migrations.RemoveField(
            model_name='projectmanager',
            name='active',
        ),
        migrations.RemoveField(
            model_name='tester',
            name='active',
        ),
        migrations.AlterField(
            model_name='executive',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ManagerDesignation'),
        ),
        migrations.AlterField(
            model_name='projectmanager',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ManagerDesignation'),
        ),
        migrations.AddField(
            model_name='designer',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Gender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='developer',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Gender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='executive',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Gender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectmanager',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Gender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tester',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Gender'),
            preserve_default=False,
        ),
    ]