# Generated by Django 3.2.19 on 2023-06-12 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cart", "0003_auto_20230612_1606"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User email ",
            ),
        ),
    ]
