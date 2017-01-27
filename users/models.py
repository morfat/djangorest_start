from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

class User(AbstractBaseUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=300)
    is_superuser=models.BooleanField(default=False)
    email=models.EmailField(max_length=200,unique=True)
    is_email_verified=models.BooleanField(default=False)
    profile_photo=models.ImageField(upload_to='users/profile_photos/%Y/%m/%d/',null=True)
    
    objects=UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    
  
        
    def get_full_name(self):
        return ('%s %s' % (self.first_name, self.last_name)).strip()
    
    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name
    