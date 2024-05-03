from django.db import models
from coach.models import *
from section.models import *


# Create your models here.
class Lesson(models.Model):
    location = models.CharField(max_length=150, verbose_name="Location")
    start_date = models.DateTimeField(verbose_name="Start time")
    end_date = models.DateTimeField(verbose_name="End time")
    coach = models.ForeignKey(Coach, verbose_name="Coach", on_delete=models.CASCADE)
    section = models.ForeignKey(
        Section, verbose_name="Section", on_delete=models.CASCADE
    )

    # def __str__(self) -> str:
    #     return self.coach

    class Meta:
        db_table = "lessons2"
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
