from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin configuration for Contact model"""
    
    list_display = ['name', 'email', 'inquiry_type', 'subject', 'created_at', 'is_responded']
    list_filter = ['inquiry_type', 'is_responded', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    list_editable = ['is_responded']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message Details', {
            'fields': ('inquiry_type', 'subject', 'message')
        }),
        ('Status & Timestamps', {
            'fields': ('is_responded', 'created_at')
        }),
    )
    
    # Make the admin interface more user-friendly
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ['name', 'email', 'phone', 'inquiry_type', 'subject', 'message']
        return self.readonly_fields
