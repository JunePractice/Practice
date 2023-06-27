from django import forms
from .models import FeedbackModel


class MyForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ["name", "telegram", "question", ]
        labels = {'name': "Как к вам обращаться?", "telegram": "Ваш никнейм в Телеграм", "question": "Введите вопрос", }
