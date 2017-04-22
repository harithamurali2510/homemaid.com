# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0019_auto_20170329_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Akshaya',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
    ]
