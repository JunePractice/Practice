from django.db import models


class FeedbackModel(models.Model):
    name = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)
    question = models.CharField(max_length=200)
