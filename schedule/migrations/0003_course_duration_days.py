# Generated by Django 4.2.2 on 2023-06-14 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_course_description_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration_days',
            field=models.DurationField(null=True),
        ),
    ]
