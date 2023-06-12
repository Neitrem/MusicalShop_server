from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(verbose_name="Item name ", max_length=255)
    description = models.CharField(verbose_name="Item decription ", max_length=255)
    cost = models.IntegerField(verbose_name="Item cost ")
    cart = models.ForeignKey(
        "cart.Cart",
        verbose_name="Cart",
        max_length=255,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    order = models.ForeignKey(
        "order.Order",
        verbose_name="Order",
        max_length=255,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    amount = models.IntegerField(verbose_name="Item amount ", default=1)

    def __str__(self) -> str:
        return str(self.pk)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Item"
        ordering = ["id", "name"]
