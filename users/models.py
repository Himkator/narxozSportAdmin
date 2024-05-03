from django.db import models
from student.models import Student
from coach.models import Coach


# Create your models here.
class Users(models.Model):
    SkFk = models.CharField(max_length=150, unique=True, verbose_name="Sk or Fk")
    password = models.CharField(max_length=2550, verbose_name="Password")
    Fio = models.CharField(verbose_name="Fio", max_length=400)
    mail = models.CharField(verbose_name="Mail", max_length=150)
    student = models.OneToOneField(
        to=Student,
        on_delete=models.CASCADE,
        verbose_name="Student_id",
        blank=True,
        null=True,
    )
    coach = models.OneToOneField(
        to=Coach,
        on_delete=models.CASCADE,
        verbose_name="Coach",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.Fio

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users2"
