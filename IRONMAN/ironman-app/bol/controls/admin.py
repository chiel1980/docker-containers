from django.contrib import admin

from controls.models import Control

# Register your models here.
# change the admin to show the number and control_objective field instead of Bol.com Object
class ControlAdmin(admin.ModelAdmin):
    list_display = ('number', 'control_object', 'framework')
    list_filter = ['number', 'framework', 'control_object']
    search_fields = ['number', 'framework', 'control_object']
admin.site.register(Control, ControlAdmin)
# show clickable links in the admin interface for evidence_url's
def show_evidence_link(self, obj):
    return '<a href="%s">%s</a>' % (obj.evidence_url, obj.evidence_url)
show_evidence_link.allow_tags = True
