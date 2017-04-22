# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0021_akshaya_distcode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AL',
        ),
        migrations.DeleteModel(
            name='ER',
        ),
        migrations.DeleteModel(
            name='ID',
        ),
        migrations.DeleteModel(
            name='KL',
        ),
        migrations.DeleteModel(
            name='KN',
        ),
        migrations.DeleteModel(
            name='KS',
        ),
        migrations.DeleteModel(
            name='KT',
        ),
        migrations.DeleteModel(
            name='KZ',
        ),
        migrations.DeleteModel(
            name='MA',
        ),
        migrations.DeleteModel(
            name='PL',
        ),
        migrations.DeleteModel(
            name='PT',
        ),
        migrations.DeleteModel(
            name='TS',
        ),
        migrations.DeleteModel(
            name='TV',
        ),
        migrations.DeleteModel(
            name='WA',
        ),
        migrations.AlterField(
            model_name='maidsignup',
            name='age',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
