from django import forms
from .models import UserPants


class PantsUploadFileForm(forms.ModelForm):
    class Meta:
        model = UserPants
        fields = ("img",)
