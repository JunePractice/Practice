from django.shortcuts import render

from courses.forms import SearchForm
from courses.models import Course, Tag, SubmitCourse
from lessons.models import Lesson


def courses(request):
    course = Course.objects.all()
    tags = Tag.objects.all()

    if request.method == 'POST':
        string = request.POST.get('search-string', False)
        if not string:
            context = {
                'course': course,
                'tags': tags
            }
            return render(request, 'courses.html', context)
        else:
            all_course = Course.objects.all()
            course = Course.objects.filter(name=string)
            tags = Tag.objects.all()
    else:
        course = Course.objects.all()
        tags = Tag.objects.all()

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
