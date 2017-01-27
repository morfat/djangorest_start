"""
Load django connection and datatbases

"""
import django
from django.conf import settings
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangorest_start.settings')
django.setup() #setup django settings

#confim you loaded the settings 
print (settings.SECRET_KEY)


