from django import forms
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import RequestContext, render_to_response
from django.utils import simplejson
from django.utils.translation import ugettext_lazy as _ 
from beer.models import Beer, BeerStyle
from venues.models import Venue

# Get a list of all the beers
def beer_list(request):
    return render_to_response('beer/beer-list.html', { 
        'beer_list': Beer.objects.all() 
    }, context_instance=RequestContext(request))

# Show the details of the beer
def beer_detail(request, id_or_slug):
    try:
        beer = Beer.objects.get(pk=id_or_slug)
    except:
        try:
            beer = Beer.objects.get(slug=id_or_slug)
        except:
            raise Http404
    
    return render_to_response('beer/beer-detail.html', { 
        'beer': beer
    }, context_instance=RequestContext(request))

# Form for a user adding a beer into the system
class BeerForm(forms.Form):
    TEXT_ATTRS = {'class':'text'}
    brewery = forms.IntegerField(widget=forms.HiddenInput())
    style = forms.IntegerField(widget=forms.HiddenInput())
    name = forms.CharField(label=_('Name'),
                widget=forms.TextInput(attrs=TEXT_ATTRS))
    abv = forms.CharField(label=_('ABV'),
                widget=forms.TextInput(attrs=TEXT_ATTRS))
    brewery_auto = forms.CharField(label=_('Brewery'),
                widget=forms.TextInput(attrs=TEXT_ATTRS))
    style_auto = forms.CharField(label=_('Style'),
                widget=forms.TextInput(attrs=TEXT_ATTRS))

# Add a beer form handler
def beer_add(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/login/?next=%s' % request.path)
    
    if request.method == 'POST':
        form = BeerForm(request.POST)
        if form.is_valid():
            b = Beer(name = form.cleaned_data['name'],
                     abv = form.cleaned_data['abv'],
                     style = BeerStyle.objects.get(pk=form.cleaned_data['style']),
                     brewery = Venue.objects.get(pk=form.cleaned_data['brewery']))
            b.save()
            return HttpResponseRedirect('/beer/%s' % b.id)
    else:
        form = BeerForm()
        
    return render_to_response('beer/beer-add.html', {
        'form': form
    }, context_instance=RequestContext(request))

# List all the styles
def style_list(request):
    return render_to_response('beer/style-list.html', {
        'style_list': BeerStyle.objects.all()
    }, context_instance=RequestContext(request))

# Get the style and all beers in the style
def style_detail(request, id_or_slug):
    try:
        style = BeerStyle.objects.get(pk=id_or_slug)
    except:
        try:
            style = BeerStyle.objects.get(slug=id_or_slug)
        except:
            raise Http404
    return render_to_response('beer/style-detail.html', { 
        'style': style,
        'beer_list': Beer.objects.filter(style=style.id),
    }, context_instance=RequestContext(request))
    
# Search beer styles and return json, primarily for autocomplete form fields
def search_styles_json(request):
    result = []
    data = BeerStyle.objects.filter(name__startswith=request.GET.get('name', ''))
    for style in data:
        result.append({'id':style.id, 'name':style.name})
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')

def search_beer_json(request):
    result = []
    data = Beer.objects.filter(name__startswith=request.GET.get('name', ''))
    for beer in data:
        result.append({'id':beer.id, 'name':beer.name})
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')