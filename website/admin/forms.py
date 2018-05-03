from django import forms

from website import models


class PhotoForm(forms.ModelForm):

    class Meta:
        model = models.Photo
        fields = (
            'original',
            'name',
            'description',
        )
