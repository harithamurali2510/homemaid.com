# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0018_auto_20170328_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maidsignup',
            old_name='code',
            new_name='cpassword',
        ),
        migrations.RemoveField(
            model_name='maidsignup',
            name='location',
        ),
        migrations.AddField(
            model_name='maidsignup',
            name='cusrname',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='maidsignup',
            name='distcode',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
