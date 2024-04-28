from django.contrib import admin

from .models import Gsearch

@admin.register(Gsearch)
class GsearchAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name')
    search_fields = ('name',)
