# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 19:55
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('builds', '0031_convert_log_data_to_json'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvironmentVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('value', models.TextField()),
                ('is_secret', models.BooleanField(default=True)),
                ('project', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='environment_variables',
                    to='builds.Project'
                )),
            ],
        ),
    ]
