# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0017_auto_20170328_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='AL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ER',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='KL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='KN',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='KS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='KT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='KZ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centre_name', models.CharField(max_length=30, blank=True)),
                ('passcode', models.CharField(max_length=30, blank=True)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='AkshayaDetails',
        ),
    ]
