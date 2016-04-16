# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assesment', '0002_auto_20160323_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk_assesment',
            name='asset_category',
            field=models.CharField(max_length=25, null=True, choices=[(b'Physical', b'Physical'), (b'Network', b'Network'), (b'Server', b'Server'), (b'Service', b'Service'), (b'Other', b'Other')]),
        ),
        migrations.AlterField(
            model_name='risk_assesment',
            name='business_impact',
            field=models.CharField(max_length=25, null=True, choices=[(b'low', b'low'), (b'medium', b'medium'), (b'high', b'high')]),
        ),
        migrations.AlterField(
            model_name='risk_assesment',
            name='control_strength',
            field=models.CharField(max_length=25, null=True, choices=[(b'low', b'low'), (b'medium', b'medium'), (b'high', b'high')]),
        ),
        migrations.AlterField(
            model_name='risk_assesment',
            name='space',
            field=models.CharField(max_length=25, null=True, choices=[(b'Platform', b'Platform'), (b'SRT Shopping', b'SRT Shopping'), (b'SRT Fulfillment', b'SRT Fulfillment'), (b'SRT Retail', b'SRT Retail'), (b'Other', b'Other')]),
        ),
    ]
