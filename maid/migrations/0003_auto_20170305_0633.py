# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0002_auto_20170304_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='email',
            new_name='e_mail',
        ),
    ]
