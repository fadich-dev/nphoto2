from django.contrib.admin import AdminSite
from django.contrib.auth.models import User

from website import models

from . import models as admin_models


class NPhotoAdminSite(AdminSite):
    site_title = 'NPhoto'
    site_header = 'NPhoto administration'
    index_title = 'Administration system'

    login_template = 'admin_panel/login.html'
    site_url = None


admin_site = NPhotoAdminSite(name='Admin Site')


admin_site.register(User)
admin_site.register(models.Photo, admin_models.PhotoAdmin)
