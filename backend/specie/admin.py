from django.contrib import admin

from .models import Specie

@admin.register(Specie)
class SpecieAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name')
    # readonly_fields = ('slug', 'created', 'modified')
    # list_display_links = ('name',)
    search_fields = ('name',)
    # list_filter = ('status',)
    # date_hierarchy = 'created'
    # ordering = ('-created',)
    # actions = ('',)


# admin.site.register(Race)
