# mgicandles/admin.py
from django.contrib import admin
from .models import MgiCandles

@admin.register(MgiCandles)
class MgiCandlesAdmin(admin.ModelAdmin):
    list_display = ('user', 'signal', 'timestamp', 'trade_signal', 'is_active')
    list_filter = ('trade_signal', 'is_active', 'user')
    search_fields = ('signal', 'user__email')  # Allows searching by signal and user's email
    prepopulated_fields = {'signal': ('signal',)}  # Prepopulate based on signal if needed
    ordering = ('-timestamp',)  # Order by timestamp descending

    # Optional: Define fieldsets to group fields in the admin form
    fieldsets = (
        (None, {
            'fields': ('user', 'signal', 'trade_signal', 'is_active')
        }),
        ('Candle Images', {
            'fields': ('idea_candle', 'line_graph_candle', 'signal_candle')
        }),
    )

    # Optional: Define which fields to show in the change view
    def get_readonly_fields(self, request, obj=None):
        if obj:  # If we are editing an existing object
            return ['user', 'timestamp']
        return super().get_readonly_fields(request, obj)

# Register the model admin with Django's admin site
