from django.shortcuts import render

# Create your views here.

def lesson(request, lesson_id):

    questions = [
        {
            'number': 1,
            'body': 'Мы считали дырки в сыре: два плюс три равно ...?',
            'answer_type': 'radio',
            'options': ['четыре', 'пять', 'шесть'],
        },
        {
            'number': 2,
            'body': 'Сколько будет 9 + 10?',
            'answer_type': 'checkbox',
            'options': ['12', '13', '19', '4'],
        },
        {
            'number': 3,
            'body': 'Сколько будет 1 + 10?',
            'answer_type': 'text',
        },
        {
            'number': 4,
            'body': 'Сколько будет 9 + 2?',
            'answer_type': 'text',
        },
    ]
    context = {
        'lesson_id': lesson_id,
        'lesson_title': f'Урок {lesson_id}',
        'questions': questions,
    }


    return render(request, 'index.html', context)
