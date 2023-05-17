from django.db import models

# Create your models here.

class Cart(models.Model):
    data = models.JSONField(verbose_name='Name ', max_length=255,)

    
    #objects = UserManager()

    
    def __str__(self) -> str:
        return str(self.pk)
    
        
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'
        ordering = ['id', 'email']