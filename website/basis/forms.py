from django import forms


class AddContactForm(forms.Form):
    email = forms.EmailField(max_length=255, label="Почта")
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 75, 'rows': 10}), label="Сообщение")
