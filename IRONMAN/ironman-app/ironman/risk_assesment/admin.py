from django.contrib import admin

from risk_assesment.models import Risk_assesment 

# Register your models here.
class Risk_assesmentAdmin(admin.ModelAdmin):
    list_display = ('space', 'threat', 'vulnerability', 'asset_category', 'residual_risk')
    list_filter = ['space', 'threat', 'vulnerability', 'asset_category']
    search_fields = ['space', 'threat', 'vulnerability', 'asset_category']
admin.site.register(Risk_assesment, Risk_assesmentAdmin)
