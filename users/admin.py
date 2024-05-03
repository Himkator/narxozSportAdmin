from django.contrib import admin
from users.models import *


# Register your models here.
@admin.register(Users)
class User2Admin(admin.ModelAdmin):
    list_display = ["SkFk", "password"]
