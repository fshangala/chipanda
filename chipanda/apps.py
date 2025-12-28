# chipanda/apps.py

from django.apps import AppConfig

class ChipandaConfig(AppConfig):
    name = 'chipanda'

    def ready(self):
        # We monkey-patch the default admin site with our custom one
        # This is the most compatible way to avoid RuntimeError
        from django.contrib import admin
        from .admin import ChipandaAdminSite
        
        # Create an instance of your custom site
        custom_site = ChipandaAdminSite()
        
        # Replace the default site globally
        admin.site.__class__ = ChipandaAdminSite
        admin.site.site_header = "Chipanda Admin"
        admin.site.site_title = "Chipanda Real Estate"
        admin.site.index_title = "Agent Management Portal"
        admin.site.base_template = "admin/base_site.html"
    