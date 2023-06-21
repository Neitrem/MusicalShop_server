# Generated by Django 4.2.1 on 2023-06-21 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Request",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("endpoint", models.CharField(max_length=100, null=True)),
                ("response_code", models.PositiveSmallIntegerField()),
                ("method", models.CharField(max_length=10, null=True)),
                ("remote_address", models.CharField(max_length=20, null=True)),
                ("exec_time", models.IntegerField(null=True)),
                ("date", models.DateTimeField(auto_now=True)),
                ("body_response", models.TextField()),
                ("body_request", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
