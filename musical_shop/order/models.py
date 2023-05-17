from django.db import models


# Create your models here.

class Order(models.Model):

    user = models.ForeignKey("User", verbose_name="User id ", on_delete=models.CASCADE)
    item = models.ForeignKey("Item", verbose_name='Name ', max_length=255, on_delete=models.CASCADE)
    status = models.CharField(verbose_name='Order status ', max_length=100, default="Created")
    
    #objects = UserManager()

    
    def __str__(self) -> str:
        return str(self.pk)
    
        
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'
        ordering = ['id', 'status']
