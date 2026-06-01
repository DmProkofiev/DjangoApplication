
# Маршрутизатор (urls.py)
from django.contrib import admin
from django.urls import path, include
from vault import views
from vault.views import account_list_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('generator/', include('vault.urls')),
    path('register/', views.register_view, name='register'),
    path('user/', views.users, name='user'),
    path('login/', views.login_view, name='login'),
    path('accounts/', views.account_list_view, name="account_list"),
    path('logout/', views.logout_view, name="logout") #новое!
]
