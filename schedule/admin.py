from django.contrib import admin

from schedule.models import Course, Review, Subscriber


admin.site.register(Course)
admin.site.register(Review)
admin.site.register(Subscriber)
