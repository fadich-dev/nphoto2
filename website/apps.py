from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class WebsiteConfig(AppConfig):
    name = 'website'

    def ready(self):
        import website.signals


class NPhotoAdminConfig(AdminConfig):
    default_site = 'website.admin.NPhotoAdminSite'
