from django.db import models

# Create your models here.

class Cart(models.Model):
    
    item = models.ForeignKey("item.Item", verbose_name='Name ', max_length=255, on_delete=models.CASCADE)
    user = models.ForeignKey("authentication.User", verbose_name="User email ", on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='Item amount ')
    
    #objects = UserManager()

    
    def __str__(self) -> str:
        return str(self.pk)
    
        
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'
        ordering = ['id', 'amount']