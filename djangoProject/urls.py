from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from schedule.views import calendar, index
from lessons.views import lesson, lesson_submit_form
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', calendar, name='calendar'),
    path('', index, name='index'),
    path('lessons/<int:lesson_id>/', lesson, name='lesson_detail'),
    path('lessons/submit-form', lesson_submit_form, name="lesson_form"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)