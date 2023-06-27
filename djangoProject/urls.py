from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from schedule.views import calendar, index
from lessons.views import lesson, lesson_submit_form
from django.conf import settings
from django.contrib.auth import views
from account import views as user_views

from feedback.views import my_form
from notification.views import notification

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', calendar, name='calendar'),
    path('', index, name='index'),
    path('myCourses/', user_views.get_my_courses, name='myCourses'),
    path('profile/', user_views.profile , name='profile'),
    path("login/", views.LoginView.as_view(next_page=''), name="login"),
    path("logout/", views.LogoutView.as_view(next_page=''), name="logout"),
    path('register/', user_views.register, name='register'),
    path('lessons/<int:lesson_id>/', lesson, name='lesson_detail'),
    path('feedback/', my_form, name='feedback'),
    path('notification/', notification, name='notification'),
    path('lessons/submit-form', lesson_submit_form, name="lesson_form"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)