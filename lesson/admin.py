from django.contrib import admin
from lesson.models import Lesson


# Register your models here.
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["location", "section", "coach"]
