try:
    from functools import update_wrapper
except ImportError:
    from django.utils.functional import update_wrapper

from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from django.utils import simplejson

# util method to 
def get_object_or_404(model_class, id):
    try:
        return model_class.objects.get(pk=id)
    except:
        raise Http404

class Respond(object):
    def __init__(self, html, json=True, request_context=True):
        self.html = html
        self.json = json;
        self.request_context = request_context

    def __call__(self, view_func):
        def wrapper(request, *args, **kwargs):
            context = view_func(request, *args, **kwargs)
            context_instance = self.request_context and RequestContext(request) or Context()
            http_accept = request.META['HTTP_ACCEPT'];
        
            if 'text/html' in http_accept and self.html != None:
                return render_to_response(self.html, context, context_instance=context_instance)
            
            elif 'application/json' in http_accept and self.json:    
                return HttpResponse(simplejson.dumps(context), mimetype='application/json')
            
            return HttpResponse(request.META['HTTP_ACCEPT'])
            
        update_wrapper(wrapper, view_func)
        return wrapper