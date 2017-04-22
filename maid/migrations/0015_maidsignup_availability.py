# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0014_auto_20170317_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='maidsignup',
            name='availability',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
