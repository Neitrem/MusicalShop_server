# Generated by Django 4.2.1 on 2023-06-22 11:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("item", "0005_item_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="cart",
        ),
    ]
