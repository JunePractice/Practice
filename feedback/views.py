from django.shortcuts import render
from .models import FeedbackModel
from .forms import MyForm
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello METANIT.COM")


def my_form(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyForm()
    return render(request, 'feedback.html', {'form': form})