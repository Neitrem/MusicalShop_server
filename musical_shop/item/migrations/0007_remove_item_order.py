# Generated by Django 4.2.1 on 2023-06-22 11:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("item", "0006_remove_item_cart"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="order",
        ),
    ]
