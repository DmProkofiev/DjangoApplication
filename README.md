# DjangoApplication — Password Generator

Учебный проект в Академии ТОП. Мое первое знакомство с фреймворком Django.

---

## Заметки

### Общие Сведения Django
Django - это фреймворк для создания веб-приложений с помощью языка программирования Python.
Django был создан в 2005 году, когда веб-разработчики из газеты Lawrence Journal-World стали использовать Python в качестве языка для создания веб-сайтов. 
А в 2008 году вышел публичный первый релиз фреймворка.      
Архитектура MVT: Model, View, Template

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

### Синтакисческие Сведения Python
```
    *args - 
```

```
    **kwargs - 
```

### Технические сведения

`INSTALLED_APPS` - это список всех приложений, которые Django включает в проект.        
Каждое приложение - это независимый модуль со своей логикой: модели (база данных), представления (views), шаблоны, статические файлы, команды

```
INSTALLED_APPS = [
    'django.contrib.admin',        # Административная панель (/admin)
    'django.contrib.auth',         # Аутентификация: пользователи, группы, права
    'django.contrib.contenttypes', # Привязка моделей друг к другу (нужен для auth и admin)
    'django.contrib.sessions',     # Управление сессиями между запросами
    'django.contrib.messages',     # Всплывающие уведомления ("Пароль изменён")
    'django.contrib.staticfiles',  # Статические файлы: CSS, JS, изображения
]
```

`MIDDLEWARE` - это список классов/функций, которые выполняются глобально для всех URL проекта. 
Они работают до того, как запрос попадёт view, и после того, как view сформирует ответ.
Типичные задачи middleware: проверка авторизации (request.user), защита от CSRF, управление сессиями, сжатие ответа, логирование всех запросов.

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',               # HTTPS, HSTS, защита заголовков
    'django.contrib.sessions.middleware.SessionMiddleware',        # Привязка сессии через cookies
    'django.middleware.common.CommonMiddleware',                   # Работа с www, слешами в URL
    'django.middleware.csrf.CsrfViewMiddleware',                   # Защита от CSRF-атак (формы, POST)
    'django.contrib.auth.middleware.AuthenticationMiddleware',     # Добавляет request.user
    'django.contrib.messages.middleware.MessageMiddleware',        # Поддержка сообщений (messages.success)
    'django.middleware.clickjacking.XFrameOptionsMiddleware',      # Защита от встраивания в iframe
]    
```

`TEMPLATES` - это настройка того, как Django загружает и обрабатывает HTML-шаблоны.       
Она определяет движок шаблонов, пути поиска файлов и набор функций (context_processors),         
которые автоматически добавляют данные (например, пользователя или запрос) в каждый шаблон.     

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Движок (почти всегда стандартный)
        'DIRS': [],                                                    # Дополнительные папки с шаблонами (вне приложений)
        'APP_DIRS': True,                                              # Искать шаблоны в папке templates/ каждого приложения
        'OPTIONS': {
            'context_processors': [                                    # Функции, которые добавляют общие переменные во все шаблоны
                'django.template.context_processors.request',          # Переменная {{ request }}
                'django.contrib.auth.context_processors.auth',         # Переменная {{ user }}
                'django.contrib.messages.context_processors.messages', # {{ messages }}
            ],
        },
    },
]
```
---

