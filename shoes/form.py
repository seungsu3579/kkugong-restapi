from django import forms
from .models import UserShoes


class ShoesUploadFileForm(forms.ModelForm):
    class Meta:
        model = UserShoes
        fields = ("img",)
