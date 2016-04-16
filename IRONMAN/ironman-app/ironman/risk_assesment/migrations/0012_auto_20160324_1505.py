# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assesment', '0011_risk_assesment_asset_example'),
    ]

    operations = [
        migrations.RenameField(
            model_name='risk_assesment',
            old_name='owner_email',
            new_name='risk_owner_email',
        ),
        migrations.RemoveField(
            model_name='risk_assesment',
            name='owner',
        ),
        migrations.AddField(
            model_name='risk_assesment',
            name='interviewee',
            field=models.CharField(default=b'name of the person being interviewed', max_length=50),
        ),
        migrations.AddField(
            model_name='risk_assesment',
            name='interviewer',
            field=models.CharField(default=b'the person who did the risk assesment', max_length=50),
        ),
        migrations.AddField(
            model_name='risk_assesment',
            name='risk_owner',
            field=models.CharField(default=b'the director who is the owner of this risk', max_length=50),
        ),
        migrations.AlterField(
            model_name='risk_assesment',
            name='threat',
            field=models.CharField(default=b'something like exploit of known vulnerabilities', max_length=75),
        ),
        migrations.AlterField(
            model_name='risk_assesment',
            name='vulnerability',
            field=models.CharField(default=b'something like missing patch management', max_length=75),
        ),
    ]
