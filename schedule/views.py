from django.shortcuts import render
from schedule.models import Review, Course
import random


def index(request):
    reviews = Review.objects.filter(rating=5)
    courses = Course.objects.all()
    random_courses = random.sample(list(courses), 3)

    context = {
        'reviews': reviews,
        'random_courses': random_courses,
    }

    return render(request, 'schedule/index.html', context)

def calendar(request):
    return render(request, 'schedule/calendar.html')
