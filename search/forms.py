from django import forms
from .models import Ad


class CreationForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'image']
