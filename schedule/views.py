from django.shortcuts import render
from schedule.models import Review, Course
import random
from django.core.mail import send_mail
from django.conf import settings
from .forms import SubscriberForm
from django.db import IntegrityError
from .models import Subscriber


def index(request):
    reviews = Review.objects.filter(rating=5)
    courses = Course.objects.all()
    random_courses = random.sample(list(courses), 3)

    message = ''
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                subscriber, created = Subscriber.objects.get_or_create(email=email)
                if created:
                    subject = 'подписка на рассылку'
                    message = 'вы успешно подписались!'
                    from_email = settings.DEFAULT_FROM_EMAIL
                    send_mail(subject, message, from_email, [email], fail_silently=False,)
            except IntegrityError:
                pass
        else:
            message = 'Вы уже подписаны!'
    else:
        form = SubscriberForm()
    context = {
        'reviews': reviews,
        'random_courses': random_courses,
        'form': form,
        'message': message,
    }
    return render(request, 'schedule/index.html', context)


def calendar(request):
    return render(request, 'schedule/calendar.html')
