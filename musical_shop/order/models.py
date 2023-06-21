from django.db import models


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        "authentication.User", verbose_name="User email ", on_delete=models.CASCADE
    )
    status = models.CharField(
        verbose_name="Order status ", max_length=100, default="Created"
    )

    # objects = UserManager()

    def __str__(self) -> str:
        return str(self.pk)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Order"
        ordering = ["id", "status"]
