from django.contrib import admin
from lessons.models import Lesson, TestQuestion, TestAnswer, TestResult
# Register your models here.

admin.site.register(Lesson)
admin.site.register(TestQuestion)
admin.site.register(TestAnswer)
admin.site.register(TestResult)
