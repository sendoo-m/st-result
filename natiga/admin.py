from django.contrib import admin
from import_export import resources
from natiga.models import Natigas
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class Natiga(resources.ModelResource):

    class Meta:
        model = Natigas

class NatigaAdmin(ImportExportModelAdmin):
    resource_class = Natiga
    search_fields = ['nationalid', 'name' , 'code']
    list_display = ['name','nationalid','total', 'seat_number']
    # list_filter = ['total']
admin.site.register(Natigas, NatigaAdmin)

