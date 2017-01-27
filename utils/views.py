from rest_framework import generics
# Create your views here.
from django.db import transaction
from django.utils.decorators import method_decorator
from django.http import Http404

#create global transactional class mixin

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
#from notifications.models import Message



class TransactionalViewMixin(object):
    """This is a global view wrapper that provides ,
    transactions and filters
    """
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,)
    @method_decorator(transaction.atomic)
    def dispatch(self, *args, **kwargs):
        return super(TransactionalViewMixin, self).dispatch(*args, **kwargs)


class ListCreateView(TransactionalViewMixin,generics.ListCreateAPIView):
    model=None
    error_message ="Error"
    success_message = "Succcess"
     
    def perform_create(self,serializer):
        #can override this 
        serializer.save()

    def get_queryset(self):
        #can override this 
        return self.model.objects.filter(is_deleted=False)



class RetrieveUpdateDestroyView(TransactionalViewMixin,generics.RetrieveUpdateDestroyAPIView):
    
    def perform_destroy(self,model_object):
        """ called by generic detail view for flagging is_deleted to True.  
        """
        model_object.is_deleted=True
        model_object.save()

  