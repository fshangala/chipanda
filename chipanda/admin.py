# chipanda/admin.py

from django.contrib import admin
from django.urls import path

class ChipandaAdminSite(admin.AdminSite):

    def get_urls(self):
        from accounts.views import AdminProfileView
        
        urls = super().get_urls()
        custom_urls = [
            path('my-profile/', self.admin_view(AdminProfileView.as_view()), name='my-profile'),
        ]
        return custom_urls + urls