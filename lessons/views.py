from django.shortcuts import render


# Create your views here.

def lesson(request, lesson_id):
    context = {
        'lesson_id': id
    }
    return render(request, 'index.html', context)
