from django.contrib import admin
from coach.models import Coach


# Register your models here.
@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin): ...
