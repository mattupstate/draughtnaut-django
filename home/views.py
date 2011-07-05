from django.shortcuts import RequestContext, render_to_response

def index(request):
    return render_to_response('home/index.html', None, context_instance=RequestContext(request))