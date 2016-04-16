# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assesment', '0007_auto_20160324_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='risk_assesment',
            old_name='asset_name',
            new_name='vulnerability',
        ),
        migrations.AlterField(
            model_name='risk_assesment',
            name='asset_category',
            field=models.CharField(max_length=25, null=True, choices=[(b'Physical', b'Physical'), (b'Network', b'Network'), (b'Server', b'Server'), (b'Service', b'Service'), (b'Software', b'Software'), (b'People', b'People'), (b'Other', b'Other')]),
        ),
    ]
