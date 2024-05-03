from django.db import models
from student.models import Student
from lesson.models import Lesson


# Create your models here.
class LessonEnroll(models.Model):
    student = models.ForeignKey(
        Student, verbose_name="Student", on_delete=models.CASCADE
    )
    lesson = models.ForeignKey(Lesson, verbose_name="Lesson", on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    attended = models.BooleanField(verbose_name="Attended")
