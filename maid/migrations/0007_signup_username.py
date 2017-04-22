# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0006_auto_20170305_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='username',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
