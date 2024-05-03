from django.contrib import admin
from lessonenroll.models import LessonEnroll


# Register your models here.
@admin.register(LessonEnroll)
class LessonnEnrollAdmin(admin.ModelAdmin):
    list_display = ["lesson", "student"]
