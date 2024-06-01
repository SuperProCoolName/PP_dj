from django import forms
from django.forms import ModelForm, TextInput, Textarea, NumberInput, FileInput
from .models import Ad


class CreationForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'image']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control__title', 'placeholder': 'Введите заголовок'}),
            'description': Textarea(attrs={'class': 'form-control__desc', 'rows': 3, 'placeholder': 'Введите описание'}),
            'price': NumberInput(attrs={'class': 'form-control__price', 'placeholder': 'Введите цену'}),
            'image': FileInput(attrs={'class': 'form-control__file'}),
        }
    def as_p(self):
        """Возвращает поля формы, рендеринг без названий полей"""
        html = ''
        for field in self.visible_fields():
            html += f'<p>{field}</p>'
        return html