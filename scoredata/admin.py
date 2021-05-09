from django.contrib import admin
from .models import Scoresp, Scoredp, CsvUpload, VersionList

# Register your models here.

admin.site.register(Scoresp)
admin.site.register(Scoredp)
admin.site.register(CsvUpload)
admin.site.register(VersionList)