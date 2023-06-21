from django.contrib.auth.models import BaseUserManager

from cart.models import Cart
from order.models import Order


class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        name,
        user_role,
        password=None,
    ):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            user_role=user_role,
            password=password
            # cart = Cart.objects.get_or_create(data={"name": "Order 1", "description": "descr"})
        )

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email=email, name=name, password=password, user_role="Admin"
        )

        user.is_superuser = True

        user.save()

        return user
