from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django.contrib.admin import widgets


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    last_name = forms.CharField(required=False)
    first_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['last_name', 'first_name']


class AccountUpdateForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    patronymic = forms.CharField(required=False)
    phone_number = forms.CharField(required=False)
    date_of_birth = forms.DateField(required=False, widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
    )

    class Meta:
        model = Account
        fields = ['date_of_birth', 'photo', 'phone_number', 'patronymic', 'gender']
