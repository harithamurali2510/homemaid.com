# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0020_akshaya'),
    ]

    operations = [
        migrations.AddField(
            model_name='akshaya',
            name='distcode',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
