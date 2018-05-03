from django.contrib.admin import ModelAdmin

from . import forms


class PhotoAdmin(ModelAdmin):
    form = forms.PhotoForm
    change_form_template = 'admin/photo_change_form.html'

    list_display = (
        'thumb',
        'name',
        'short_description',
    )

    search_fields = (
        'name',
        'description',
    )

    def short_description(self, obj):
        return '{}{}'.format(obj.description[:127], '...' if len(obj.description) > 127 else '')
