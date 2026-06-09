import secrets
import string
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import length
from vault.forms import RegisterForm, AccountForm
from .models import Account

# Генерация паролей
def generate_password(length=16, use_digits=True, use_special=True):
# базовый алфовит-буквы в обоих регистрах(A-Z, a-z)
    alphabet=string.ascii_letters
    if use_digits:
        alphabet+=string.digits
    if use_special:
        alphabet+= "!@#$%^&*-_=+"
    return ''.join(secrets.choice(alphabet) for i in range(length))

def _password_option(request):
    """
    Считывает из GET параметров сложности
    и при необходиомсти генерирует пароль.
    Возвращаемый словарь полей:
        -gen_length: текущая длина (для подстановки в input)
        -gen_digits: включены ли цифры (для чекбокса)
        -gen_special: включены ли спецсимволы (для чекбокса)
        -generated_password: сгенерирован пароль или None
    Пароль создается: только если в GET явно есть generate=1
    (нажата кнопка Сгенерировать)
    """
    is_generate = request.GET.get('generate')=='1'
    #Длина пароля
    try:
        length=int(request.GET.get('length', '16'))
    except (TypeError, ValueError):
        length = 16

    # ограничиваем разумным диапазоном: чтобы не сломать форму
    length = max(4, min(length, 128))
    if is_generate:
        use_digits=request.GET.get('digits')=='on'
        use_special=request.GET.get('special')=='on'
        password=generate_password(
            length=length,
            use_digits=use_digits,
            use_special=use_special
        )
    else:
        use_digits = True
        use_special = True
        password=None

    return {
        "gen_length": length,
        "gen_digits": use_digits,
        "gen_special": use_special,
        "generated_password": password
    }

# Статика
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

# Обработка валидации
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

def account_create_view(request):
    """
    Добавление новой учетной записи
    """
    if request.method=="POST":
        form=AccountForm(request.POST)
        if form.is_valid():
            # coomit = False - создаем обьект, но пока не сохраняем в БД
            account=form.save()
            # привязываем УЗ к текущему пользавателю
            account.owner=request.user
            account.save()
            return redirect('account_list')
        opts = _password_option(request)
    else:
        opts = _password_option(request)
        initial = {}
        if opts['generated_password']:
            initial['password']=opts['generated_password']
        form = AccountForm(initial=initial)

    context = {"form": form}
    return render(request, template_name="vault/account_form.html", context=context)

def account_detail_view(request, pk):
    account = Account.objects.filter(pk=pk)
    context = {"account": account}
    return render(request, template_name="vault/account_detail.html")

def account_edit_view(request, pk):
    account = get_object_or_404(Account, pk=pk, owner=request.user)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect("account_detail", pk=account.pk)
        opts = _password_option(request)
    else:
        opts = _password_option(request)
        if opts["generated_password"]:
            form = AccountForm(
                instance=account,
                initial={"password": opts["generated_password"]}
            )
        else:
            opts = _password_option(request)
            if opts["generated_password"]:
                form = AccountForm(
                    instance=account,
                    initial={"password": opts["generated_password"]}
                )
            else:
                form=AccountForm(instance=account)
    return render(request,"vault/account_form.html",{"form": form, **opts})


