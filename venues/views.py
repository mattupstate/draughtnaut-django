from django import forms
from django.http import Http404, HttpResponse
from django.shortcuts import RequestContext, render_to_response
from django.utils import simplejson 
from venues.models import Venue, VenueType
from beer.models import Beer, BeerOnTap
import logging

# Show all the venues in a list
def venue_list(request):
    return render_to_response('venues/venue-list.html', { 
        'venue_list': Venue.objects.all() 
    }, context_instance=RequestContext(request))

# Show a venue in detail, including any beers made at the venue
def venue_detail(request, id_or_slug):
    try:
        venue = Venue.objects.get(pk=id_or_slug)
    except:
        try:
            venue = Venue.objects.get(slug=id_or_slug)
        except:
            raise Http404
    
    return render_to_response('venues/venue-detail.html', { 
        'venue': venue,
        'beer_list': Beer.objects.filter(brewery=venue.id),
        'beer_on_tap': BeerOnTap.objects.filter(venue=venue.id),
    }, context_instance=RequestContext(request))

# Shows all the venue types in a list
def type_list(request):
    return render_to_response('venues/type-list.html', { 
        'type_list': VenueType.objects.all() 
    }, context_instance=RequestContext(request))

# Shows all the venues of a certain type
def type_detail(request, id_or_slug):
    try:
        type = VenueType.objects.get(pk=id_or_slug)
    except:
        try:
            type = VenueType.objects.get(slug=id_or_slug)
        except:
            raise Http404
    
    return render_to_response('venues/type-detail.html' , { 
        'type': type,
        'venue_list': Venue.objects.filter(venue_type=type.id),
    }, context_instance=RequestContext(request))
    
# Search venues and return json, primarily for autocomplete form fields
def search_json(request):
    result = []
    data = Venue.objects.filter(name__startswith=request.GET.get('name', ''))
    for venue in data:
        result.append({'id':venue.id, 'name':venue.name})
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')

# Add a beer on tap
def add_beer_ontap(request):
    if not request.user.is_authenticated():
        return
     
    result = {}
    try:
        beer_id = request.POST.get('beer_id')
        venue_id = request.POST.get('venue_id')
    except:
        result = { 'error':'Form error.' }
        
    try:
        BeerOnTap.objects.get(beer=beer_id, venue=venue_id)
        result = { 'error':'This beer is already on tap here.' }
    except:
        pass
        
    try:
        b = Beer.objects.get(pk=beer_id)
        v = Venue.objects.get(pk=venue_id)
        ontap = BeerOnTap(added_by=request.user, beer=b, venue=v)
        ontap.save()
        result = { 'id':ontap.id, 'name':b.name }
    except:
        result = { 'error':'Invalid beer or venue.' }
    
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    
# Remove a beer on tap
def remove_beer_ontap(request):
    if not request.user.is_authenticated():
        return 
    
    result = {}
    try:
        ontap_id = request.POST.get('id')
        BeerOnTap.objects.get(pk=ontap_id).delete()
        result = { 'id':ontap_id }
    except:
        result = { 'error':'Form error or item does not exist.' }
    
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    