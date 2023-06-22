from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .manager import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="User email ", max_length=255, unique=True)
    name = models.CharField(
        verbose_name="Name ",
        max_length=255,
    )
    city = models.CharField(verbose_name='City ', max_length=255, default='Moscow')
    phone = models.CharField(verbose_name='Phone ', max_length=20, default='+7 910 313 11 44')
    birth_date = models.CharField(verbose_name='Birth date ', max_length=255, default='10.03.1995')

    user_role = models.CharField(
        verbose_name="User role ", max_length=255, null=True, blank=True, default="user"
    )

    is_staff = models.BooleanField(verbose_name="Is staff", default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self) -> str:
        return str(self.email)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["id", "email"]
