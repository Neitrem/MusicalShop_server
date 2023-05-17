from django.contrib.auth.models import BaseUserManager

from cart.models import Cart
from order.models import Order

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None):
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            cart = Cart.objects.get_or_create(data={"name": "Order 1", "description": "descr"})
        )
        


        user.set_password(password)
        
        user.save()
        
        return user
    
    def create_superuser(self, email, first_name, password):
        user = self.create_user(
            email = email,
            first_name = first_name,
            password = password
        )
        
        user.is_superuser = True
        
        user.save()
        
        return user