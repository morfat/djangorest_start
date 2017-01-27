from rest_framework.renderers import JSONRenderer
from rest_framework import status

class CustomJSONRenderer(JSONRenderer):
    """System wide custom renderer . this formats data for response """
    
    def get_response_message(self,renderer_context):
        response=renderer_context.get('response')
        view = renderer_context['view']
        message,state='',''
        if not response:
            return [message,state]
        
        if response.status_code in [status.HTTP_200_OK,status.HTTP_201_CREATED]:
            #message=renderer_context.get(view.success_message,'Successful')
            try:
                message = view.success_message
            except:
                message = "Successfully"
            state=True
        else:
            #message=renderer_context.get(view.error_message,'Ooops something went please Try again Later')
            try:

                message = view.error_message
            except:
                message = "Ooops something went Wrong."
            state=False

        return [message,state]
    
        
    def render(self, data, accepted_media_type=None, renderer_context=None):
        message,state=self.get_response_message(renderer_context)    
        
        data = {'data': data,'message':message,'status':state}  
      
              
        
        return super(CustomJSONRenderer, self).render(data, accepted_media_type, renderer_context)
    