from django.conf.urls import url

from .views import *

urlpatterns=[
            url('^$',UserList.as_view()),
            url('^(?P<pk>[0-9]+)/$',UserDetail.as_view()),
             ]
