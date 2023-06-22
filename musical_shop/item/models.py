from django.db import models

# Create your models here.


class Item(models.Model):
    GIT = "GUITAR"
    AMP = "AMP"
    ACC = "ACCESSUAR"

    ITEM_TYPES = (
        (GIT, "Guitar"),
        (AMP, "Amp"),
        (ACC, "Accessuar"),
    )
    
    image = models.ImageField(verbose_name="Item image ", upload_to='images', null=True)
    
    name = models.CharField(verbose_name="Item name ", max_length=255)
    description = models.CharField(verbose_name="Item decription ", max_length=255)
    cost = models.IntegerField(verbose_name="Item cost ")
    type = models.CharField(verbose_name='Item type', max_length=255, choices=ITEM_TYPES, default=GIT)
    
    
    amount = models.IntegerField(verbose_name="Item amount ", default=1)

    def __str__(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Item"
        ordering = ["id", "name"]
