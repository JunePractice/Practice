from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=200, null=True)
    full_description = models.TextField(null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    tag = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=0, null=True)
    duration_days = models.PositiveIntegerField(null=True)
    course_image = models.ImageField(upload_to='images/courses', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'
        ordering = ['time_create']