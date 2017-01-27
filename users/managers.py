import random
import string
from django.contrib.auth.base_user import BaseUserManager
#from utils.notifications import Message


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email,password, **extra_fields):
        #do validations
        random_password=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
        
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.is_active=True
        user.save(using=self._db)
        #Message.create_email(message=message,recipient_address=email,template_id=template_id)
        return user
        


    def create_user(self, email,password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,password,**extra_fields)
        
    
   
    

    def create_superuser(self, email,password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email,password, **extra_fields)
        
        

