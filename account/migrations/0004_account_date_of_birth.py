# Generated by Django 4.2.2 on 2023-06-25 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_account_last_name_remove_account_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
