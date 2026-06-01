from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from vault.forms import RegisterForm
from .models import Account

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

# def register_view(request):
#     form=RegisterForm()
#     context = {"form": form}
#     return render(request, 'vault/register.html', context=context)

def register_view(request) -> HttpResponse:
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, "vault/register.html", context)


def login_view(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            error = "Неверный логин или пароль"

    return render(request, "vault/login.html", context={"error": error})

def account_list_view(request):
    """
    страница со списком учетных записей
    """
    accounts = Account.objects.filter(owner=request.user)
    context = {"account": accounts}
    return render(request, template_name="vault/account_list.html", context=context)

def logout_view(request):
    logout(request)
    return redirect('login')



