# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Risk_assesmentl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('space', models.CharField(blank=True, max_length=25, null=True, choices=[(b'Platform', b'Platform'), (b'SRT Shopping', b'SRT Shopping'), (b'SRT Fulfillment', b'SRT Fulfillment'), (b'SRT Retail', b'SRT Retail'), (b'Other', b'Other')])),
                ('asset_name', models.CharField(max_length=25)),
                ('asset_category', models.CharField(blank=True, max_length=25, null=True, choices=[(b'Physical', b'Physical'), (b'Network', b'Network'), (b'Server', b'Server'), (b'Service', b'Service'), (b'Other', b'Other')])),
                ('business_impact', models.CharField(blank=True, max_length=25, null=True, choices=[(b'low', b'low'), (b'medium', b'medium'), (b'high', b'high')])),
                ('business_impact_remark', models.CharField(max_length=500)),
                ('control_strength', models.CharField(blank=True, max_length=25, null=True, choices=[(b'low', b'low'), (b'medium', b'medium'), (b'high', b'high')])),
                ('control_strength_remark', models.CharField(max_length=500)),
                ('owner', models.CharField(max_length=200)),
                ('owner_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
