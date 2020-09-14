from django import forms
from .models import UserTops


class TopUploadFileForm(forms.ModelForm):
    class Meta:
        model = UserTops
        fields = ("img",)

