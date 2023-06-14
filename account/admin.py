from django.contrib import admin
from .models import Account

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']

admin.site.register(Account, ProfileAdmin)