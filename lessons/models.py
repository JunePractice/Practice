from django.db import models

from courses.models import Course


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    lesson_length = models.CharField(max_length=8)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уроки курсов'
        verbose_name_plural = 'Уроки курсов'
