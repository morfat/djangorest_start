from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class EmailAuthTokenSerializer(serializers.Serializer):
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})
    email = serializers.CharField(label=_("Email"))
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs
    
