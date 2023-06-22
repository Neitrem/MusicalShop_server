from django.db import models


# Create your models here.


class Order(models.Model):
    DEL = "DELIVERED"
    PAI = "PAID"
    CAN = "CANCELED"

    ORDER_STATUSES = (
        (DEL, "Delivered"),
        (PAI, "Paid"),
        (CAN, "Canceled"),
    )
    
    
    user = models.ForeignKey(
        "authentication.User", verbose_name="User email ", on_delete=models.CASCADE
    )
    status = models.CharField(
        verbose_name="Order status ", max_length=100, choices=ORDER_STATUSES, default=PAI
    )
    item = models.ForeignKey(
        "item.Item",
        verbose_name="Item",
        max_length=255,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    
    amount = models.IntegerField(verbose_name="Amount of items ", default=1)


    # objects = UserManager()

    def __str__(self) -> str:
        return str(self.user.email)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Order"
        ordering = ["id", "status"]
