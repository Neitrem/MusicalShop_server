# Generated by Django 4.2.1 on 2023-06-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0004_order_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="amount",
            field=models.IntegerField(default=1, verbose_name="Amount of items "),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("DELIVERED", "Delivered"),
                    ("PAID", "Paid"),
                    ("CANCELED", "Canceled"),
                ],
                default="PAID",
                max_length=100,
                verbose_name="Order status ",
            ),
        ),
    ]
