# Generated by Django 4.2.2 on 2023-06-14 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_last_name_account_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='name',
        ),
    ]