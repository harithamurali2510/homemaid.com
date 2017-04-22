# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0003_auto_20170305_0633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='e_mail',
            new_name='email',
        ),
    ]
