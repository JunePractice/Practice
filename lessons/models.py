from django.db import models
# from courses.models import Course
from django.contrib.auth.models import User


# удалить, когда будет создана модель courses.models.Course
class Course(models.Model):
    pass


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    lesson_length = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video_url = models.CharField(max_length=255)


class TestQuestion(models.Model):
    test = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    body = models.TextField()
    answer_type = models.CharField(max_length=255)
    answer_options = models.TextField()


class TestResult(models.Model):
    username = models.CharField(max_length=255)
    test = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class TestAnswer(models.Model):
    result = models.ForeignKey(TestResult, on_delete=models.CASCADE, related_name='answers')
    test_question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    answer = models.TextField()
