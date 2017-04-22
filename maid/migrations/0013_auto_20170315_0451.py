# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0012_maidsignup_work_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maidsignup',
            name='dcode',
        ),
        migrations.AlterField(
            model_name='maidsignup',
            name='location',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
