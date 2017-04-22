# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0009_auto_20170307_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsignup',
            name='address',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='clientsignup',
            name='age',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='clientsignup',
            name='gender',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='clientsignup',
            name='name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='clientsignup',
            name='phone',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='maidsignup',
            name='address',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='maidsignup',
            name='age',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='maidsignup',
            name='field',
            field=models.CharField(max_length=15, blank=True),
        ),
        migrations.AddField(
            model_name='maidsignup',
            name='gender',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='maidsignup',
            name='location',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='maidsignup',
            name='name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='maidsignup',
            name='phone',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
