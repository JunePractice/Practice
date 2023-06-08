from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'schedule/index.html')

def calendar(request):
    return render(request, 'schedule/calendar.html')
