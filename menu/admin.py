from django.contrib import admin
from .models import SubSuperMenu, SuperMenu

@admin.register(SubSuperMenu)
class SubAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']
    search_fields = ['title', 'type']

@admin.register(SuperMenu)
class SuperMenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_domain']
    search_fields = ['title', 'domain__domain']
    filter_horizontal = ['sub']

    def get_domain(self, obj):
        return obj.domain.domain
    get_domain.short_description = 'Domain'
