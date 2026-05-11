# DjangoApplication    
`Академия ТОП`             
# Учебный проект Password_Generator - мое знакомство с Django        

`Заметки`     
# Commnad Promt Git: Windows PowerShell       
git init                          # Создать новый репозиторий в текущей папке       
git clone <url>                   # Склонировать удалённый репозиторий      
git status                        # Показать состояние файлов (что изменено, что не отслеживается)      
git add .                         # Добавить все изменения      
git commit -m "сообщение"         # Зафиксировать изменения с комментарием      
git push                          # Отправить коммиты в удалённый репозиторий (origin)      
git push -u origin main           # Первый пуш с привязкой локальной ветки main к удалённой     
git pull                          # Забрать и слить изменения с удалённого репозитория      
git branch                        # Показать список локальных веток     
git checkout -b имя_ветки         # Создать новую ветку и сразу на неё переключиться        
git checkout имя_ветки            # Переключиться на существующую ветку     
git merge имя_ветки               # Влить указанную ветку в текущую     
git log --oneline                 # Просмотр истории коммитов (короткий формат)     
git remote add origin <url>       # Привязать локальный репозиторий к удалённому        
git restore имя_файла             # Отменить изменения в файле (сбросить до последнего коммита)     
git reset HEAD имя_файла          # Убрать файл из индекса (отмена git add)     
git rm --cached имя_файла         # Перестать отслеживать файл (с удалением из индекса, но не с диска)      
        
# Commnad Promt Django: Windows PowerShell      
django-admin startproject django_password_generator . #Создание Django - проекта      
python.exe .\manage.py startapp vault #новое приложение модуль с именем vault внутри проекта     
python.exe .\manage.py makemigrations #Генерация файлов миграций на основе изменений в моделях       
python.exe .\manage.py migrate #Реализация миграций к БД или обновление      
python.exe .\manage.py runserver #запуск сервера локально        