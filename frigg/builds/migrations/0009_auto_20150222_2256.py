# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0008_auto_20150216_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='private',
            field=models.BooleanField(default=True, db_index=True),
            preserve_default=True,
        ),
    ]
