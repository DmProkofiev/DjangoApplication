from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AccountForm(forms.ModelForm):
    # Данные создания\редактирования Учетной Записи
    class Meta:
        # с какой моделью связываем форму
        model = Account
        # какие поля нужно отобразить
        fields = ('site', 'login', 'password')

# Форма регистрации
class RegisterForm(UserCreationForm):
    model = User
    fields = ('username', )