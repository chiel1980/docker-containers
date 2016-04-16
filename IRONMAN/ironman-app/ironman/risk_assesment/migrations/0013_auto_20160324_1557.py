# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assesment', '0012_auto_20160324_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk_assesment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='risk_assesment',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
