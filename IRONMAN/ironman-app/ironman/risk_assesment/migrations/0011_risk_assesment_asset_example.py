# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assesment', '0010_auto_20160324_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk_assesment',
            name='asset_example',
            field=models.CharField(default=b'something like gerrit or ams5 or kevlar', max_length=50),
        ),
    ]
