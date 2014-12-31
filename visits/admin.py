from django.contrib import admin
from visits.models import VisitCount, BlacklistedIP, BlacklistedUserAgent


class VisitCountAdmin(admin.ModelAdmin):
    list_display = ('item', 'visit_count', 'created_at')
    list_filter = list()
    list_editable = list()
    search_fields = list()
    ordering = ["item_type", "-visit_count"]
    prepopulated_fields = {}
    fieldsets = [
        (None, {
            'fields': (
                'visit_count',
            ),
        }),
    ]


class BlacklistedIPAdmin(admin.ModelAdmin):
    pass


class BlacklistedUserAgentAdmin(admin.ModelAdmin):
    pass


admin.site.register(VisitCount, VisitCountAdmin)
admin.site.register(BlacklistedIP, BlacklistedIPAdmin)
admin.site.register(BlacklistedUserAgent, BlacklistedUserAgentAdmin)
