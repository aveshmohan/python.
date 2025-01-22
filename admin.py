from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from app import models

# Register your models here.
admin.site.register(models.Hospital)


# class HospitalAdmin(ImportExportModelAdmin):
#     list_display= 'name'
