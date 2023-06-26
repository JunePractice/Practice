from django.shortcuts import render

from courses.forms import SearchForm
from courses.models import Course, Tag, SubmitCourse
from lessons.models import Lesson


def courses(request):
    course = Course.objects.all()
    tags = Tag.objects.all()

    if request.method == 'POST':
        string = request.POST.get('search-string', False)
        checkboxes = request.POST.getlist('check-filter', False)
        print(checkboxes)
        if checkboxes:
            if checkboxes == ['OneWeek']:
                course = Course.objects.filter(duration_days__lt=7)
            elif checkboxes == ['ThreeWeek'] or checkboxes == ['OneWeek', 'ThreeWeek']:
                course = Course.objects.filter(duration_days__lt=21)
            elif checkboxes == ['MoreThreeWeek']:
                course = Course.objects.filter(duration_days__gt=21)
            elif checkboxes == ['Free']:
                course = Course.objects.filter(price=0)
            elif checkboxes == ['Free', 'OneWeek']:
                course = Course.objects.filter(duration_days__lt=7, price=0)
            elif checkboxes == ['Free', 'ThreeWeek'] or checkboxes == ['Free', 'OneWeek', 'ThreeWeek']:
                course = Course.objects.filter(duration_days__lt=21, price=0)
            elif checkboxes == ['Free', 'MoreThreeWeek']:
                course = Course.objects.filter(duration_days__gt=21, price=0)
            else:
                course = Course.objects.all()

        elif not string:
            context = {
                'course': course,
                'tags': tags
            }
            return render(request, 'courses.html', context)

        else:
            course = Course.objects.filter(name=string)
    else:
        course = Course.objects.all()

    context = {
        'course': course,
        'tags': tags
    }
    return render(request, 'courses.html', context)


def current_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        string = request.POST.get('phone', False)
        print(string)
        if string != -1:
            sub = SubmitCourse()
            sub.phone_number = string
            sub.course = course
            sub.save()

    lessons = course.lesson_set.all()

    context = {
        'course': course,
        'lessons': lessons
    }
    return render(request, 'course.html', context)


def tag_course(request, tag_id):
    tag = Tag.objects.select_related().get(id=tag_id)
    course = tag.course_set.all()
    print(course)

    context = {
        'tagCourses': course
    }

    return render(request, 'tag-course.html', context)
