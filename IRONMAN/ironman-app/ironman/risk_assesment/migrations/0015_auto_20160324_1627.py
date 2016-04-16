# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assesment', '0014_auto_20160324_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk_assesment',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
