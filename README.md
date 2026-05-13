# DjangoApplication — Password Generator

Учебный проект в Академии ТОП. Мое первое знакомство с фреймворком Django.

---

## Заметки

### Git PyCharm
| Команда                | Описание                       |
|------------------------|--------------------------------|
| `python -m venv .venv` | Создать виртуальное окружени   |
| `.venv\Scripts\Activate.ps1` | Активать вирт окружение        |

### Git (Windows PowerShell)

| Команда | Описание |
|---------|----------|
| `git init` | Создать новый репозиторий в текущей папке |
| `git clone <url>` | Склонировать удалённый репозиторий |
| `git status` | Показать состояние файлов (изменённые, неотслеживаемые) |
| `git add .` | Добавить все изменения в индекс |
| `git commit -m "сообщение"` | Зафиксировать изменения с комментарием |
| `git push` | Отправить коммиты |
| `git push -u origin main` | Первый пуш с привязкой локальной ветки main к удалённой |
| `git pull` | Забрать и слить изменения с удалённого репозитория |
| `git branch` | Показать список локальных веток |
| `git checkout -b имя_ветки` | Создать новую ветку и сразу на неё переключиться |
| `git checkout имя_ветки` | Переключиться на существующую ветку |
| `git merge имя_ветки` | Влить указанную ветку в текущую |
| `git log --oneline` | Просмотр истории коммитов (короткий формат) |
| `git remote add origin <url>` | Привязать локальный репозиторий к удалённому |
| `git restore имя_файла` | Отменить изменения в файле (сбросить до последнего коммита) |
| `git reset HEAD имя_файла` | Убрать файл из индекса (отмена git add) |
| `git rm --cached имя_файла` | Перестать отслеживать файл (удалить из индекса, оставить на диске) |

---

### Django (Windows PowerShell)

| Команда | Описание |
|---------|----------|
| `django-admin startproject django_password_generator .` | Создание Django-проекта в текущей папке |
| `python.exe .\manage.py startapp vault` | Создание приложения vault внутри проекта |
| `python.exe .\manage.py makemigrations` | Генерация файлов миграций на основе изменений в моделях |
| `python.exe .\manage.py migrate` | Применение миграций к базе данных |
| `python.exe .\manage.py runserver` | Запуск сервера http://127.0.0.1:8000 |

Для остановки сервера **Ctrl + C**

### Технические сведения

список всех приложений (модулей), которые активны       
Django использует этот список, чтобы знать, какие модели, шаблоны, статические файлы и команды нужно загрузить.     
INSTALLED_APPS = [      
    'django.contrib.admin', # Административная панель (сайт /admin)     
    'django.contrib.auth', # Система аутентификации: пользователи, группы, права, пароли        
    'django.contrib.contenttypes', # Фреймворк для "привязки" моделей друг к другу (нужен для auth и admin)     
    'django.contrib.sessions', # Управление сессиями (сохраняет состояние пользователя между запросами)     
    'django.contrib.messages', # Однострочные всплывающие сообщения ("Пароль изменён", "Статья сохранена")      
    'django.contrib.staticfiles', # Обработка статических файлов: CSS, JS, изображения
]       

промежуточное программное обеспечение — это "слои" обработки,       
через которые проходит каждый HTTP-запрос от браузера и HTTP-ответ от сервера       
MIDDLEWARE = [      
    'django.middleware.security.SecurityMiddleware', # Безопасность: HTTPS-редиректы, заголовки HSTS, XSS-защита        
    'django.contrib.sessions.middleware.SessionMiddleware', # Привязывает сессию к каждому запросу (через cookies)      
    'django.middleware.common.CommonMiddleware', # Перенаправления с www и без, обработка PREPEND_WWW, APPEND_SLASH     
    'django.middleware.csrf.CsrfViewMiddleware', # Защита от CSRF-атак (подделка межсайтовых запросов) — важен для форм и POST-запросов     
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Привязывает текущего пользователя к запросу (request.user)     
    'django.contrib.messages.middleware.MessageMiddleware', # Поддерживает систему однострочных сообщений (messages.success(request, "..."))        
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Защита от clickjacking (встраивания вашего сайта в iframe злоумышленником)      
]       


---

