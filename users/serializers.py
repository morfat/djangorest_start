from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs={'password':{'write_only':True}}
        
    def create(self,validated_data): 
        password=validated_data.pop('password')
        email=validated_data.pop('email')
        user=User.objects.create_user(email=email,password=password,**validated_data)
        
        return user
