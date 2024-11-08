from django.contrib import admin
from FilterApp.models import FilterModel
# Register your models here.
class FilterModelAdmin(admin.ModelAdmin):
    list_display=['name','eCount','subject','dept','date']
admin.site.register(FilterModel,FilterModelAdmin)