# Generated by Django 3.2.19 on 2023-06-12 13:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_alter_order_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="item",
        ),
    ]