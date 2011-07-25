from django.shortcuts import RequestContext, render_to_response

def main_index(request):
    return render_to_response('main/main-index.html', None, context_instance=RequestContext(request))