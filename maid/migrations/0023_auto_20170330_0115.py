# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0022_auto_20170329_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='maidsignup',
            name='imagename',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='maidsignup',
            name='uploaded_file_url',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
