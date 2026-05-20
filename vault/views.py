from django.shortcuts import render
from urllib3 import request

from vault.forms import RegisterForm


# Обработчик  обрабатывает запрос и возвращает ответ
def home(request):
    return render(request, 'vault/home.html')

def about(request):
    return render(request, 'vault/about.html')

def contact(request):
    return render(request, 'vault/contact.html')

def help(request):
    return render(request, 'vault/help.html')

def users(request):
    return render(request, 'vault/user.html')

def register_view(request):
    form=RegisterForm()
    context = {"form": form}
    return render(request, 'vault/register.html', context=context)
