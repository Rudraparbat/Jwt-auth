# Generated by Django 5.1.3 on 2024-11-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authers', '0003_alter_authuser_phone_numbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='date_of_birth',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
