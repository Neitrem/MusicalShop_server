# Generated by Django 4.2.1 on 2023-06-22 10:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0006_user_birth_date_user_city_user_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=True, verbose_name="Is staff"),
        ),
    ]
