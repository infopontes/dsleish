from django.contrib import admin

from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'breed')
    # readonly_fields = ('slug', 'created', 'modified')
    # list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('breed',)
    # date_hierarchy = 'created'
    # ordering = ('-created',)
    # actions = ('',)


# admin.site.register(Race)
