from django.shortcuts import render
from schedule.models import Review


def index(request):
    reviews = Review.objects.filter(rating=5)
    context = {'reviews': reviews}

    return render(request, 'schedule/index.html', context)

def calendar(request):
    return render(request, 'schedule/calendar.html')
