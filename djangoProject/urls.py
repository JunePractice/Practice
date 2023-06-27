from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from schedule.views import calendar, index
from django.conf import settings
from django.contrib.auth import views
from account import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', calendar, name='calendar'),
    path('', index, name='index'),
    path('profile/', user_views.profile , name='profile'),
    path("login/", views.LoginView.as_view(next_page=''), name="login"),
    path("logout/", views.LogoutView.as_view(next_page=''), name="logout"),
    path('register/', user_views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)