from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(max_length=255, label="Почта")
    message = forms.CharField(widget=forms.Textarea(), label="Сообщение")
