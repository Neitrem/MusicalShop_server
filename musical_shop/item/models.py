from django.db import models

# Create your models here.

class Item(models.Model):

    

    name = models.CharField(verbose_name='Item name ', max_length=255)
    description = models.CharField(verbose_name='Item decription ', max_length=255)
    cost = models.IntegerField(verbose_name='Item cost ', max_length=255)

    def __str__(self) -> str:
        return str(self.pk)
    
        
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Item'
        ordering = ['id', 'name']