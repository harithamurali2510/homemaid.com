# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0010_auto_20170307_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maidsignup',
            name='age',
            field=models.CharField(max_length=5, blank=True),
        ),
    ]
