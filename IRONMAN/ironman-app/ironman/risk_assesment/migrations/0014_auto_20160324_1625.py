# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assesment', '0013_auto_20160324_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='risk_assesment',
            old_name='modified_date',
            new_name='modified',
        ),
        migrations.RemoveField(
            model_name='risk_assesment',
            name='created_date',
        ),
        migrations.AddField(
            model_name='risk_assesment',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
