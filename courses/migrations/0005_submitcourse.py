# Generated by Django 4.2.2 on 2023-06-26 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_course_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
            options={
                'verbose_name': 'Номера и курсы',
                'verbose_name_plural': 'Номера и курсы',
            },
        ),
    ]
