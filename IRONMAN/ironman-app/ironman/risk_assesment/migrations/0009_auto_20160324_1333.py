# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assesment', '0008_auto_20160324_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk_assesment',
            name='asset_category',
            field=models.CharField(max_length=25, null=True, choices=[(b'Data-center', b'Data-center'), (b'Office', b'Office'), (b'Network', b'Network'), (b'Server', b'Server'), (b'Service', b'Service'), (b'Software', b'Software'), (b'People', b'People'), (b'Other', b'Other')]),
        ),
    ]
