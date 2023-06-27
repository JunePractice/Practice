from django.db import models


class NotificationModel(models.Model):
    text = models.CharField(max_length=200)
