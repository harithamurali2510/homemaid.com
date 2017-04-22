# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0008_auto_20170307_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maidsignup',
            name='email',
        ),
        migrations.AddField(
            model_name='maidsignup',
            name='code',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='maidsignup',
            name='dcode',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
