# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0013_auto_20170315_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maidsignup',
            name='age',
            field=models.IntegerField(blank=True),
        ),
    ]
