# Generated by Django 4.2.2 on 2023-06-26 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_submitcourse_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submitcourse',
            name='course_name',
        ),
    ]
