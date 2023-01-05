from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import *
# Register your models here.

# admin.site.register(Leads)
# @admin.register(Leads)
# class ViewAdmin(ImportExportModelAdmin):
#     exclude = ('id', )


class LeadsResource(resources.ModelResource):

    class Meta:
        model = Leads
        # exclude = ('id', )



class LeadsAdmin(ImportExportModelAdmin):

    resource_classes = [LeadsResource]

admin.site.register(Leads, LeadsAdmin)