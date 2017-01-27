
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserSerializer
from .serializers import EmailAuthTokenSerializer
from utils.renderers import CustomJSONRenderer
from utils.views import TransactionalViewMixin
from rest_framework.permissions import  AllowAny

class ObtainExpiringAuthToken(TransactionalViewMixin,views.ObtainAuthToken):
    
    serializer_class = EmailAuthTokenSerializer
    permission_classes = (AllowAny,)
    renderer_classes = (CustomJSONRenderer, )
    authentication_classes = ()
  
    def get_token(self,user):
    
        try:
            Token.objects.get(user=user).delete()
        except: #token failed delete/or not exist
            pass
        finally:
            
            return Token.objects.create(user=user)

       
    def post(self, request):
        serializer =self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            token=self.get_token(user=serializer.validated_data['user'])
            return Response({'token': token.key,'user':UserSerializer(token.user).data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

obtain_expiring_auth_token = ObtainExpiringAuthToken.as_view()
