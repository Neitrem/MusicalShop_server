from django.db import models

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField("authentication.User", verbose_name="User email ", on_delete=models.CASCADE)
    
    #objects = UserManager()

    
    def __str__(self) -> str:
        return str(self.pk)
    
        
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'
        ordering = ['id']