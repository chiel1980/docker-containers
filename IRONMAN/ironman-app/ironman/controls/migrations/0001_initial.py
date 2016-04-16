# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('IT_or_Financial', models.CharField(blank=True, max_length=10, null=True, choices=[(b'Financial', b'Financial'), (b'IT', b'IT')])),
                ('framework', models.CharField(max_length=25, choices=[(b'ISO-27001', b'ISO-27001'), (b'PCI-DSS', b'PCI-DSS'), (b'SOx', b'SOx'), (b'RBAC', b'RBAC'), (b'Privacy', b'Privacy'), (b'PCI-DSS and SOx', b'PCI-DSS and SOx'), (b'PCI-DSS, SOx and RBAC', b'PCI-DSS, SOx and RBAC'), (b'All', b'All'), (b'None', b'None')])),
                ('number', models.CharField(max_length=7)),
                ('risk', models.CharField(max_length=200)),
                ('control_objective', models.CharField(max_length=200)),
                ('control_object', models.CharField(max_length=200)),
                ('control_area', models.CharField(max_length=200)),
                ('control_description', models.CharField(max_length=200)),
                ('expected_results', models.CharField(max_length=250, blank=True)),
                ('owner', models.CharField(max_length=200)),
                ('owner_email', models.EmailField(max_length=254)),
                ('delegate', models.CharField(max_length=200)),
                ('frequency', models.CharField(max_length=10, choices=[(b'daily', b'daily'), (b'weekly', b'weekly'), (b'monthly', b'monthly'), (b'quarterly', b'quarterly'), (b'annual', b'annual'), (b'occurence', b'occurence'), (b'automatic', b'automatic')])),
                ('tested_by_IA', models.CharField(blank=True, max_length=3, null=True, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('evidence_ticket', models.CharField(max_length=12, blank=True)),
                ('evidence_link', models.URLField(blank=True)),
                ('January_ticket', models.CharField(max_length=200, blank=True)),
                ('February_ticket', models.CharField(max_length=200, blank=True)),
                ('March_ticket', models.CharField(max_length=200, blank=True)),
                ('April_ticket', models.CharField(max_length=200, blank=True)),
                ('May_ticket', models.CharField(max_length=200, blank=True)),
                ('June_ticket', models.CharField(max_length=200, blank=True)),
                ('July_ticket', models.CharField(max_length=200, blank=True)),
                ('August_ticket', models.CharField(max_length=200, blank=True)),
                ('September_ticket', models.CharField(max_length=200, blank=True)),
                ('October_ticket', models.CharField(max_length=200, blank=True)),
                ('November_ticket', models.CharField(max_length=200, blank=True)),
                ('December_ticket', models.CharField(max_length=200, blank=True)),
            ],
        ),
    ]
