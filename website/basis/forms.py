from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Почта')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={"cols": 48, "rows": 16}))
    captcha = CaptchaField(label='Captcha')
