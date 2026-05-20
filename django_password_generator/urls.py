
# Маршрутизатор (urls.py)
from django.contrib import admin
from django.urls import path, include
from vault import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('generator/', include('vault.urls')),
    path('register/', views.register_view, name='register'),
    # конструкция Django, которая подключает все маршруты (URL-ы) из другого файла — а именно из vault/urls.py.
    # Она используется для модульной организации маршрутов, когда проект разрастается и маршрутов становится много

    path('user/', views.users, name='user'),
]
