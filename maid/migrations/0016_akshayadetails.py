# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0015_maidsignup_availability'),
    ]

    operations = [
        migrations.CreateModel(
            name='AkshayaDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('code', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
    ]
