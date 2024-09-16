from django.contrib import admin

from .models import Collect

@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id_animal')
    # readonly_fields = ('slug', 'created', 'modified')
    # list_display_links = ('name',)
    search_fields = ('dt_collection',)
    list_filter = ('dt_collection',)
    # date_hierarchy = 'created'
    # ordering = ('-created',)
    # actions = ('',)


# admin.site.register(Race)
