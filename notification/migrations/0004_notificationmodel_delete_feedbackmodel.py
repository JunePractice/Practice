# Generated by Django 4.2.2 on 2023-06-27 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='FeedbackModel',
        ),
    ]