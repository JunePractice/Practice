from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from schedule.views import calendar, index
from lessons.views import lesson
from django.conf import settings
from courses.views import courses, current_course, tag_course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', calendar, name='calendar'),
    path('', index, name='index'),
    path('courses/', courses, name='courses'),
    path('courses/<int:course_id>/', current_course, name='current-course'),
    path('courses/tag/<int:tag_id>/', tag_course, name='courses'),
    path('lessons/<int:lesson_id>/', lesson, name='lesson_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)