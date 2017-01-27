
from rest_framework import generics
from users.serializers import *
from users.models import User
from django.db import transaction
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import random,string
from rest_framework.parsers import FormParser, MultiPartParser,JSONParser
from utils.renderers import CustomJSONRenderer
from rest_framework.permissions import IsAuthenticated,AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.core.exceptions import ValidationError
from utils.views import TransactionalViewMixin


class UserList(TransactionalViewMixin,generics.ListCreateAPIView):
    """ used for user signup """
    #error_message =" "
    #success_messgae = ""
    serializer_class=UserSerializer
    renderer_classes = (CustomJSONRenderer, )
    permission_classes = (AllowAny,)
    authentication_classes = ()
    
    filter_fields = ('first_name','last_name','id_number','email','phone_number','business','level',)
    
    search_fields=('first_name','last_name','id_number','email','phone_number','level',)
    
    def perform_create(self,serializer):
        serializer.save()

    def get_queryset(self):
        return User.objects.filter(is_active=True)
    


class UserDetail(TransactionalViewMixin,generics.RetrieveUpdateAPIView):
    """ you can also mmake partial updates using PUT. 
    if password field is provided, the password will change. but no email/ notification will be sent to User
    regarding the changes
    """

    serializer_class=UserSerializer
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    
    renderer_classes = (CustomJSONRenderer, )
    
    queryset=User.objects.all()

   
    
    def put(self, request, pk, format=None):
        user = self.get_object()
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            valid_data = serializer.validated_data
            serializer.save()

            if valid_data.get('password'):
                user.set_password(valid_data.get('password'))
                user.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_destroy(self,model_object):
        model_object.is_active=True
        model_object.save()


 
   