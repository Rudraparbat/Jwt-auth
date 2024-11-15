# Generated by Django 5.1.3 on 2024-11-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('authers', '0004_alter_authuser_date_of_birth'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authuser',
            options={},
        ),
        migrations.AddConstraint(
            model_name='authuser',
            constraint=models.UniqueConstraint(fields=('username',), name='unique_username'),
        ),
    ]