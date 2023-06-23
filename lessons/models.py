from django.db import models
# from courses.models import Course

# удалить, когда будет создана модель courses.models.Course
class Course(models.Model):
    pass

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description=models.TextField()
    lesson_length = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)