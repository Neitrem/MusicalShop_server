# Generated by Django 3.2.19 on 2023-06-12 13:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0002_alter_cart_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cart",
            options={
                "ordering": ["id"],
                "verbose_name": "Cart",
                "verbose_name_plural": "Cart",
            },
        ),
        migrations.RemoveField(
            model_name="cart",
            name="amount",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="item",
        ),
    ]
