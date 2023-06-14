from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=7, decimal_places=0, null=True)
    duration_days = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, f'{i}') for i in range(1, 6)])
    description = models.TextField()

    def __str__(self):
        return f'{self.user.username} оставил(а) отзыв на курс "{self.course.name}"'
    class Meta:
        ordering = ['-rating']