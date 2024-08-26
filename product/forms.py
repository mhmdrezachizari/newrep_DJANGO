from django import forms
from .models import FORMSSEARCHMODEL
class FORMSEARCH(forms.ModelForm):
    class Meta:
        model = FORMSSEARCHMODEL
        fields = ('name',)