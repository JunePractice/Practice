from django.shortcuts import render

from courses.models import Course


def courses(request):
    course = Course.objects.all()
    context = {
        'course': course
    }
    return render(request, 'courses.html', context)


def current_course(request, course_id):
    return render(request, 'courses.html')
