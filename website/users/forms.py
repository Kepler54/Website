from django import forms
from django.contrib.auth import get_user_model
from users.context_processors import get_categories
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class AddPostForm(forms.Form):
    post_title = forms.CharField(max_length=40, label="Заголовок: ")
    post_content = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 75, 'rows': 10}), required=False, label="Текст статьи: "
    )
    photo = forms.ImageField(required=False, label="Фото: ")
    slug = forms.CharField(max_length=255, label="Слаг: ")
    category = forms.ModelChoiceField(get_categories(), label="Категории: ", empty_label="Категория не выбрана")
    is_published = forms.BooleanField(required=False, initial=True, label="Статус: ")


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин: ", widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="Пароль: ", widget=forms.PasswordInput(attrs={"class": "form-input"}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Логин: ", widget=forms.TextInput(attrs={"class": "form-input"}))
    email = forms.CharField(label="Электронная почта: ", widget=forms.EmailInput(attrs={"class": "form-input"}))
    password1 = forms.CharField(label="Пароль: ", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повтор пароля: ", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email
