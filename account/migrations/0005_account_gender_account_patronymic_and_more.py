# Generated by Django 4.2.2 on 2023-06-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_account_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('man', 'man'), ('woman', 'woman')], default='man', max_length=255),
        ),
        migrations.AddField(
            model_name='account',
            name='patronymic',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
