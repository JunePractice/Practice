from django.forms import ModelForm, TextInput
from .models import Course, SubmitCourse


class SearchForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', ]
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Введите название курса'})
        }


class SubForm(ModelForm):
    class Meta:
        model = SubmitCourse
        fields = ['phone_number', ]
        widgets = {
            'phone_number': TextInput(attrs={'placeholder': 'Введите номер телефона'})
        }
