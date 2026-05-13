from django.contrib import admin
from .models import Account

@admin.register(Account)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('site', 'login', 'owner', 'created_at', 'password_change_at')
    search_fields = ('site', 'login')
    list_filter = ('owner', )


