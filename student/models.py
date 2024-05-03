from django.db import models

# from users.models import Users2


# Create your models here.
class Student(models.Model):
    image = models.ImageField(
        upload_to="student_images", blank=True, null=True, verbose_name="Picture"
    )
    # user = models.OneToOneField(
    #     to=Users2, verbose_name="User_id", on_delete=models.CASCADE
    # )

    class Meta:
        db_table = "student2"
        verbose_name = "Student"
        verbose_name_plural = "Students"
