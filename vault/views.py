from django.shortcuts import render
from vault.forms import RegisterForm
# `View (представление) `— это функция (или класс),
# которая решает, что увидит пользователь, когда перейдёт по определённому адресу на вашем сайте.
# render() — это функция-помощник (shortcut) из django.shortcuts,
# которая загружает HTML-шаблон,
# подставляет в него данные из контекста и возвращает объект HttpResponse (готовую HTML-страницу).,
# которая объединяет шаблон (HTML) и контекст (данные), а затем возвращает готовую HTML-страницу.

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
