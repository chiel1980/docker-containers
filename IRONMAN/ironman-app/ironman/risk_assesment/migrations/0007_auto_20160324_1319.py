# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assesment', '0006_auto_20160323_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk_assesment',
            name='asset_category',
            field=models.CharField(max_length=25, null=True, choices=[(b'Physical', b'Physical'), (b'Network', b'Network'), (b'Server', b'Server'), (b'OS', b'OS'), (b'Service', b'Service'), (b'Software', b'Software'), (b'People', b'People'), (b'PII', b'PII'), (b'Payment information', b'Payment information'), (b'Other', b'Other')]),
        ),
    ]
