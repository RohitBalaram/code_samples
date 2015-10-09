# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ats', '0005_auto_20150817_0045'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AllNYCSchools',
        ),
    ]
