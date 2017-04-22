# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0011_auto_20170308_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='maidsignup',
            name='work_type',
            field=models.CharField(max_length=15, blank=True),
        ),
    ]
