# Generated by Django 4.2.1 on 2023-06-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0006_cart_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="amount",
            field=models.IntegerField(default=1, verbose_name="Amount of item "),
        ),
    ]