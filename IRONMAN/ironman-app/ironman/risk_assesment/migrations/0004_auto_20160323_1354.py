# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assesment', '0003_auto_20160323_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk_assesment',
            name='asset_category',
            field=models.CharField(max_length=25, null=True, choices=[(b'Physical', b'Physical'), (b'Network', b'Network'), (b'Server', b'Server'), (b'Service', b'Service'), (b'People', b'People'), (b'Other', b'Other')]),
        ),
        migrations.AlterField(
            model_name='risk_assesment',
            name='asset_name',
            field=models.CharField(max_length=50),
        ),
    ]
