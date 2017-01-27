from django.db.models import Q
from users.models import User

class CustomBackend(object):
    """authenticate when given email,phone number or secret key and password """
    
    def get_by_secret_key(self,key,password):
        try:
           # Try to fetch the user by searching the username or email field
            #user = User.objects.get(Q(phone_number=phone_number)|Q(email=email)|Q(secret_key=secret_key))
            
            user = User.objects.get(secret_key=key)
            if password:
                if user.check_password(password):
                    return user
            else:
                return user
        except User.DoesNotExist:
            pass
        
    def get_by_email(self,email,password):
        try:
           # Try to fetch the user by searching the username or email field
            #user = User.objects.get(Q(phone_number=phone_number)|Q(email=email)|Q(secret_key=secret_key))
            
            user = User.objects.get(email=email)
            if password:
                if user.check_password(password):
                    return user
            else:
                return user
        except User.DoesNotExist:
            pass


    def get_by_phone_number(self,phone_number,password):
        try:
            user = User.objects.get(phone_number=phone_number)
            return (user if user.check_password(password) else None) if password else None
        except User.DoesNotExist:
            pass

        
    def authenticate(self, email=None, phone_number=None,secret_key=None,password=None, **kwargs):
        
        if email:
            return self.get_by_email(email, password)
        elif phone_number:
            return self.get_by_phone_number(phone_number,password)
        elif secret_key:
            return self.get_by_secret_key(secret_key, password)
        else:
            return None
            
        
        
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
        
        
        
        