from django.db import models


# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.CharField(max_length=255, verbose_name="Description")
    max_student = models.PositiveIntegerField(verbose_name="Max student")

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "sections2"
        verbose_name = "Section"
        verbose_name_plural = "Sections"
