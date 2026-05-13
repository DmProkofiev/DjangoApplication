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


INSTALLED_APPS - Список всех приложений (модулей), которые загружает Django.  
На основе этого списка фреймворк определяет, какие модели, шаблоны, статические файлы и команды должны быть доступны.

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

MIDDLEWARE - слои обработки запросов
Промежуточное программное обеспечение (middleware) — это слои, через которые последовательно проходят каждый HTTP-запрос (от браузера) и каждый HTTP-ответ (от сервера).
Порядок следования middleware важен: они выполняются сверху вниз для запроса и в обратном порядке для ответа.

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

---

