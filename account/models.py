from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Account(models.Model):
    MAN = 'мужчина'
    WOMAN = 'женщина'

    GENDER = (
        (MAN, MAN),
        (WOMAN, WOMAN)
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='account/%Y/%m/%d', blank=True, default='account/default_icon.png')
    patronymic = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER, default=MAN)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def save(self):
        super().save()
