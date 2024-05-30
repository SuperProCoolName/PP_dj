from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input__field', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input__field', 'placeholder': 'Пароль', }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''  # Удаляем двоеточия после названий полей

    def as_p(self):
        """Возвращает поля формы, рендеринг без названий полей"""
        html = ''
        for field in self.visible_fields():
            html += f'<p>{field}</p>'
        return html
