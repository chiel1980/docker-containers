# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assesment', '0009_auto_20160324_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk_assesment',
            name='threat',
            field=models.CharField(default=b'something like exploit of known vulnerabilities', max_length=50),
        ),
        migrations.AlterField(
            model_name='risk_assesment',
            name='vulnerability',
            field=models.CharField(default=b'something like missing patch management', max_length=50),
        ),
    ]
