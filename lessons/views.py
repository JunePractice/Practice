from django.shortcuts import render

# Create your views here.

def lesson(request, lesson_id):
    # сейчас есть только лекции 0 и 1, ( /lessons/0 и /lessons/1 )

    questionss = \
    [
        [
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
        ],

        [
            {
                'number': 1,
                'body': 'Как жизнь?',
                'answer_type': 'text',
            },
        ]
    ]

    video_urls = [
        "https://www.youtube.com/embed/GmESG58YRnY",
        "https://www.youtube.com/embed/2GgiZZhO-PA",
    ]

    videos = [
        {
            'url': "https://www.youtube.com/embed/GmESG58YRnY",
            'width': '560px',
            'height': '315px',
        },
        {
            'url': "https://www.youtube.com/embed/2GgiZZhO-PA",
            'width': '560px',
            'height': '315px',
        },

    ]

    context = {
        'video': videos[lesson_id],
        'video_url': video_urls[lesson_id],
        'lesson_id': lesson_id,
        'lesson_title': f'Урок {lesson_id}',
        'questions': questionss[lesson_id],
    }


    return render(request, 'index.html', context)
