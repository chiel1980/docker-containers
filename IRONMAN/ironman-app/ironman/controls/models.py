from django.db import models

# Create your models here.

#
### drop down menu for choice of control framework
FRAMEWORK = (
    ('ISO-27001', 'ISO-27001'),
    ('PCI-DSS', 'PCI-DSS'),
    ('SOx', 'SOx'),
    ('RBAC', 'RBAC'),
    ('Privacy', 'Privacy'),
    ('PCI-DSS and SOx', 'PCI-DSS and SOx'),
    ('PCI-DSS, SOx and RBAC', 'PCI-DSS, SOx and RBAC'),
    ('All', 'All'),
    ('None', 'None'),
)
#
### drop down menu for choice of frequency
FREQUENCY = (
    ('daily', 'daily'),
    ('weekly', 'weekly'),
    ('monthly', 'monthly'),
    ('quarterly', 'quarterly'),
    ('annual', 'annual'),
    ('occurence', 'occurence'),
    ('automatic', 'automatic'),
)
### drop down menu for choice of tested by Internal Audit (IA)
IATESTED = (
    ('yes', 'yes'),
    ('no', 'no'),
)
### drop down menu for choice of financial or IT related control
FINIT = (
    ('Financial', 'Financial'),
    ('IT', 'IT'),
)

class Control(models.Model):
    IT_or_Financial = models.CharField(choices=FINIT, max_length=10, blank=True, null=True)
    framework = models.CharField(choices=FRAMEWORK, max_length=25)
    number = models.CharField(max_length=7)
    risk = models.CharField(max_length=200)
    control_objective = models.CharField(max_length=200)
    control_object = models.CharField(max_length=200)
    control_area = models.CharField(max_length=200)
    control_description = models.CharField(max_length=200)
    expected_results = models.CharField(max_length=250, blank=True, null=False)
    owner = models.CharField(max_length=200)
    owner_email = models.EmailField()
    delegate = models.CharField(max_length=200)
    frequency = models.CharField(choices=FREQUENCY, max_length=10)
    tested_by_IA = models.CharField(choices=IATESTED, max_length=3, blank=True, null=True)
    evidence_ticket = models.CharField(max_length=12, blank=True) 
    evidence_link = models.URLField(blank=True)
    January_ticket = models.CharField(max_length=200, blank=True)
    February_ticket = models.CharField(max_length=200, blank=True)
    March_ticket = models.CharField(max_length=200, blank=True)
    April_ticket = models.CharField(max_length=200, blank=True)
    May_ticket = models.CharField(max_length=200, blank=True)
    June_ticket = models.CharField(max_length=200, blank=True)
    July_ticket = models.CharField(max_length=200, blank=True)
    August_ticket = models.CharField(max_length=200, blank=True)
    September_ticket = models.CharField(max_length=200, blank=True)
    October_ticket = models.CharField(max_length=200, blank=True)
    November_ticket = models.CharField(max_length=200, blank=True)
    December_ticket = models.CharField(max_length=200, blank=True)
