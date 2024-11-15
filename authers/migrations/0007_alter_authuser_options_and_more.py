# Generated by Django 5.1.3 on 2024-11-15 09:38

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authers', '0006_alter_authuser_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveConstraint(
            model_name='authuser',
            name='unique_username',
        ),
        migrations.AlterField(
            model_name='authuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]