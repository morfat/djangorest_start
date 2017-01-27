
from users.models import User

class CustomBackend(object):
    """authenticate when given email,phone number or secret key and password """
    

    def get_by_email(self,email,password):
        try:
            user = User.objects.get(email=email)
            if password:
                if user.check_password(password):
                    return user
            else:
                return user
        except User.DoesNotExist:
            pass


    def authenticate(self, email=None, password=None, **kwargs):
        if email:
            return self.get_by_email(email, password)
        return None
            
        
        
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
        
        
        
        