# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0016_akshayadetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='akshayadetails',
            name='passcode',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='akshayadetails',
            name='code',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
