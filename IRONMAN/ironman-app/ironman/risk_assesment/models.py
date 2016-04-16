from django.db import models
from django.utils import timezone # fix erorr "global name 'timezone' is not defined"
from datetime import datetime
#
### drop down menu for choice of control framework
SPACE = (
    ('Platform', 'Platform'),
    ('SRT Shopping', 'SRT Shopping'),
    ('SRT Fulfillment', 'SRT Fulfillment'),
    ('SRT Retail', 'SRT Retail'),
    ('Other', 'Other'),
)
ASSET_CATEGORY = (
    ('Data-center', 'Data-center'),
    ('Office', 'Office'),
    ('Network', 'Network'),
    ('Server', 'Server'),
    ('Service', 'Service'),
    ('Software', 'Software'),
    ('People', 'People'),
    ('Other', 'Other'),
)
BUSINESS_IMPACT = (
    ('low', 'low'),
    ('medium', 'medium'),
    ('high', 'high'),
)
CONTROL_STRENGTH = (
    ('low', 'low'),
    ('medium', 'medium'),
    ('high', 'high'),
)
## the rest of the model
class Risk_assesment(models.Model):
    space = models.CharField(choices=SPACE, max_length=25, blank=False, null=True)
    vulnerability = models.CharField(max_length=75, default='something like missing patch management')
    threat = models.CharField(max_length=75, default='something like exploit of known vulnerabilities')
    asset_category = models.CharField(choices=ASSET_CATEGORY, max_length=25, blank=False, null=True)
    asset_example = models.CharField(max_length=50, default='something like gerrit or ams5 or kevlar')
    business_impact = models.CharField(choices=BUSINESS_IMPACT, max_length=25, blank=False, null=True)
    business_impact_remark = models.CharField(max_length=500)
    control_strength = models.CharField(choices=CONTROL_STRENGTH, max_length=25, blank=False, null=True)
    control_strength_remark = models.CharField(max_length=500)
    risk_owner = models.CharField(max_length=50, default = 'the director who is the owner of this risk')
    risk_owner_email = models.EmailField()
    interviewer = models.CharField(max_length=50, default= 'the person who did the risk assesment')
    interviewee = models.CharField(max_length=50, default = 'name of the person being interviewed')
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)
	
    # calculate residual risk
    _business_impact_score = {
        'high' : 3,
        'medium' : 2,
        'low': 1
    }
    _control_strength_score = {
        'high' : 1,
        'medium' : 2,
        'low': 3
    }
    @property
    def residual_risk(self):
        bscore = self._business_impact_score[self.business_impact]
        cscore = self._control_strength_score[self.control_strength]
        if bscore == None or cscore == None:
            return -1
        return bscore * cscore
    class ReportBuilder:
	#exclude = ()  # Lists or tuple of excluded fields
	fields =  ('space','vulnerability','threat', 'asset_category','asset_example','business_impact','business_impact_remark','control_strength_remark','risk_owner','risk_owner_email','residual_risk','interviewer','interviewee','created','modified', 'control_strength')   # Explicitly allowed fields
	extra = ('residual_risk')    # List extra fields (useful for methods)
