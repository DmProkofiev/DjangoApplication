from django.shortcuts import render

# Обработчик  обрабатывает запрос и возвращает ответ
def home(request):
    return render(request, "vault/home.html")


def views():
    return None