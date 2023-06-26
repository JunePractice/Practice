from django.shortcuts import render
from lessons.models import Lesson, TestResult, TestAnswer
from django.http import HttpResponseRedirect
# Create your views here.

def lesson(request, lesson_id):
    this_lesson = Lesson.objects.get(id=lesson_id)

    questions = [{
        'id': question.id,
        'number': i + 1,
        'body': question.body,
        'answer_type': question.answer_type,
        'answer_options': question.answer_options.split(';')
    } for i, question in enumerate(this_lesson.questions.all())]

    context = {
        'video': {
            'url': this_lesson.video_url,
            'width': '560px',
            'height': '315px',
        },
        'lesson_id': lesson_id,
        'lesson_title': this_lesson.name,
        'questions': questions,
    }

    return render(request, 'index.html', context)


def lesson_submit_form(request):
    if request.method == 'POST':
        lesson_id = request.POST.get('lesson_id')
        this_lesson = Lesson.objects.get(id=lesson_id)
        questions = this_lesson.questions.all()
        tr = TestResult(username=request.POST.get('username'), test=this_lesson)
        tr.save()
        for question in questions:
            answer = ';'.join(request.POST.getlist(f'question{question.id}', default=[]))
            TestAnswer(result=tr, test_question=question, answer=answer).save()
    return HttpResponseRedirect('/')