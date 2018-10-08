from django.contrib import admin
from gps_data.models import RawData

class RawDataAdmin(admin.ModelAdmin):
    class Meta:
        model = RawData

admin.site.register(RawData, RawDataAdmin)