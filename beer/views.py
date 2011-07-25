from django.http import Http404, HttpResponse 
from django.forms import model_to_dict
from beer.forms import ContributeBeerForm
from beer.models import Beer, BeerStyle
from venues.models import Venue
from utils.http import get_object_or_404, Respond

def _with_beer_form(context, form=None):
    form = ContributeBeerForm() if form == None else form
    context['contribute_beer_form'] = form
    return context;

# Get a list of all the beers
@Respond('beer/beer-index.html', json=True)
def beer_index(request):
    if request.method == 'GET':
        return _with_beer_form({ 
            'beer_list': Beer.objects.filter(retired=False) 
        })
    elif request.method == 'POST' and request.user.is_authenticated():
        # add a beer to be moderated
        form = ContributeBeerForm(request.POST)
        if form.is_valid():
            b = Beer(name = form.cleaned_data['name'],
                     abv = form.cleaned_data['abv'],
                     style = BeerStyle.objects.get(pk=form.cleaned_data['style']),
                     brewery = Venue.objects.get(pk=form.cleaned_data['brewery']),
                     contributed_by = request.user, 
                     approved = False)
            b.save()
            return { 'success': True }
        
        return _with_beer_form({ 'success': False }, form)
    
    raise Http404

@Respond('beer/beer-show.html')
def beer_show(request, id):
    return {
        'beer': model_to_dict(get_object_or_404(Beer, id), ['name', 'abv', 'style','brewery'])
    }
    
@Respond('beer/beer-search.html')
def beer_search(request):
    return {}

@Respond('beer/style-index.html')
def styles_index(request):
    return {}

@Respond('beer/style-show.html')
def styles_show(request):
    return {}

@Respond(None, json=True)
def styles_search(request):
    return {}