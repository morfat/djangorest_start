from users.serializers import *
from users.models import User
from utils.views import ListCreateView,RetrieveUpdateDestroyView

class UserList(ListCreateView):
    """ used for user signup """

    serializer_class=UserSerializer
    #permission_classes = (AllowAny,)
    #authentication_classes = ()
    
    filter_fields = ('first_name','last_name','email',)
    
    search_fields=('first_name','last_name','email',)
    
    def perform_create(self,serializer):
        serializer.save()

    def get_queryset(self):
        self.success_message='Retrieved'
        return User.objects.filter(is_active=True)
    


class UserDetail(RetrieveUpdateDestroyView):
    """ you can also mmake partial updates using PUT. 
    if password field is provided, the password will change. but no email/ notification will be sent to User
    regarding the changes
    """

    serializer_class=UserSerializer
    queryset=User.objects.all()


    def perform_destroy(self,model_object):
        model_object.is_active=True
        model_object.save()


 
   