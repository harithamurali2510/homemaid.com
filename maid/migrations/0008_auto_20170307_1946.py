# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0007_signup_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientSignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MaidSignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
