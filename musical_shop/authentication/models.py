from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from authentication.manager import UserManager

from cart.models import Cart
from order.models import Order


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(verbose_name='User email ', max_length=255, unique=True)
    name = models.CharField(verbose_name='Name ', max_length=255,)
    
    user_role = models.CharField(verbose_name='User role ', max_length=255, null=True, blank=True, default='user')
    
    is_superuser = models.BooleanField(verbose_name='Is superuser', default=False)
    
    objects = UserManager()
    

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self) -> str:
        return str(self.email)
    
        
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id', 'email']
