# listings/admin.py

from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    """
    Allows for the addition of multiple PropertyImage objects directly within the Property admin page.
    """
    model = PropertyImage
    extra = 1 # Provides one empty slot for a new image by default
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    # What fields to display in the main list view
    list_display = (
        'id',
        '__str__', # Uses the dynamically generated string from the __str__ method
        'property_type',
        'price',
        'bedrooms',
        'self_contained',
        'list_date',
        'agent',
    )
    
    # Fields to link to the detail change form from the list view
    list_display_links = (
        'id',
        '__str__',
    )
    
    # Fields to filter the list by on the right sidebar
    list_filter = (
        'property_type',
        'province',
        'city',
        'self_contained',
        'water_onsite',
        'toilet_type',
        'agent',
    )
    
    # Fields to search across
    search_fields = (
        'province',
        'city',
        'area',
        'price',
    )

    # Organize fields in the detail change form using fieldsets
    fieldsets = (
        ('Financials and Status', {
            'fields': ('agent', 'property_type', 'price'),
            'description': 'Set the agent and whether the property is for rent or sale.'
        }),
        ('Physical Details', {
            'fields': (
                ('bedrooms', 'bathrooms'),
                ('self_contained', 'water_onsite'),
                'toilet_type',
            ),
            'description': 'Key details about the structure and utilities.'
        }),
        ('Location', {
            'fields': ('province', 'city', 'area'),
            'description': 'Geographic information for searchability.'
        }),
        ('Metadata', {
            'fields': ('list_date',),
            'classes': ('collapse',), # Makes this section collapsible
        }),
    )

    # Add the inline model to the Property admin
    inlines = [PropertyImageInline]

    # Make the list_date field read-only as it's set automatically
    readonly_fields = ('list_date',)