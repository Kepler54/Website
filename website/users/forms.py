import datetime
from django import forms
from django.contrib.auth import get_user_model
from users.context_processors import get_categories
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class AddPostForm(forms.Form):
    post_title = forms.CharField(max_length=40, label="Заголовок: ")
    post_content = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 100, 'rows': 25}), required=False, label="Текст статьи: "
    )
    photo = forms.ImageField(required=False, label="Фото: ")
    slug = forms.CharField(max_length=255, label="Слаг: ")
    category = forms.ModelChoiceField(get_categories(), required=False, label="Категории: ",
                                      empty_label="Категория не выбрана")
    is_published = forms.BooleanField(required=False, initial=True, label="Статус: ")


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин: ", widget=forms.TextInput())
    password = forms.CharField(label="Пароль: ", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Логин: ", widget=forms.TextInput())
    email = forms.CharField(label="Почта: ", widget=forms.EmailInput())
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


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(label="Изменить логин: ", widget=forms.TextInput())
    email = forms.CharField(label="Изменить почту: ", widget=forms.EmailInput())
    this_year = datetime.date.today().year
    date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year - 150, this_year - 5))))

    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'date_birth', 'first_name', 'last_name']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'})
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Текущмй пароль: ", widget=forms.PasswordInput())
    new_password1 = forms.CharField(label="Новый пароль: ", widget=forms.PasswordInput())
    new_password2 = forms.CharField(label="Подтверждение пароля: ", widget=forms.PasswordInput())
