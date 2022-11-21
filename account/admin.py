from django.contrib import admin
from .models import CustomUser


# Register your models here.
class UserDisplay(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']

admin.site.register(CustomUser, UserDisplay)