from rest_framework import serializers
from authentication.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ('is_superuser', 'user_permissions', 'cart')
        
    def create(self, data):
        password = data.pop('password', None)
        instance = self.Meta.model(**data)
        instance.is_active = True

        if password is not None:
            instance.set_password(password)
        instance.save()
        
        print(instance.user_role)
            
        
        return instance 
      