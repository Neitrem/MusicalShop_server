from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0003_remove_order_item"),
        ("cart", "0004_alter_cart_user"),
        ("item", "0003_auto_20230612_1637"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="cart",
            field=models.ForeignKey(
                blank=True,
                max_length=255,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="cart.cart",
                verbose_name="Cart",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="order",
            field=models.ForeignKey(
                blank=True,
                max_length=255,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="order.order",
                verbose_name="Order",
            ),
        ),
    ]
