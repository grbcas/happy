# Generated by Django 5.0.3 on 2024-05-03 23:46

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_birthday'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='name'),
        ),
    ]
