from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *

# -----------------------------------------------------------------------------------------------------------------------
# Класс для обработки формы не связанной с моделью
# class AddPostForm(forms.Form):  # Класс для отображения формы на странице. Формирует необходимые теги.
#    title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'}))  # Добавляет класс 'form-input' в формирование тэга
#    slug = forms.SlugField(max_length=255, label="URL")
#    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Контент')
#    is_published = forms.BooleanField(label='Публикация', required=False, initial=True)
#    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Категория не выбрана")
# -----------------------------------------------------------------------------------------------------------------------


class AddPostForm(forms.ModelForm):
    """ Класс для обработки формы, связанной с моделью """

    def __init__(self, *args, **kwargs):    # Конструктор формы
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women           # Связь модели с формой
        # fields = '__all__'      # Какие поля необходимо отобразить в форме.
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']      # Какие поля необходимо отобразить в форме.
        widgets = {                                                    # Добавление аттрибутов для тегов
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_title(self):     # Пользовательский валидатор, для поля title
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-input'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-input'}),  #  Не работает
        #     'password2': forms.PasswordInput(attrs={'class': 'form-input'}),  #  Не работает
        #     'email': forms.EmailInput(attrs={'class': 'form-input'}),  # Не работает
        # }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()
