from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, RequestContext
from django.utils.translation import ugettext_lazy as _

def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/login')
    return HttpResponseRedirect('/users/profile')

def login_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    
    form = AuthenticationForm(None, request.POST or None)
    next = request.GET.get('next', '/')
    
    if form.is_valid():
        login(request, form.get_user())
        return HttpResponseRedirect(next)
        
    return render_to_response('users/login.html', {
        'form': form
    }, context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/login/?next=%s' % request.path)
    
    return render_to_response('users/user-profile.html', {
        'profile': request.user.get_profile(),
    }, context_instance=RequestContext(request))

def public_profile(request, id_or_username):
    try:
        user = User.objects.get(pk=id_or_username)
    except:
        try:
            user = User.objects.get(username=id_or_username)
        except:
            raise Http404
    
    return render_to_response('users/user-profile.html', {
        'profile': user.get_profile()
    }, context_instance=RequestContext(request))

class SignUpForm(forms.Form):
    TEXT_ATTRS = {'class':'text'}
    first_name = forms.CharField(label=_("First Name"), widget=forms.TextInput(attrs=TEXT_ATTRS))
    last_name = forms.CharField(label=_("Last Name"), widget=forms.TextInput(attrs=TEXT_ATTRS))
    email = forms.CharField(label=_("Email"), widget=forms.TextInput(attrs=TEXT_ATTRS))
    username = forms.CharField(label=_("Username"), widget=forms.TextInput(attrs=TEXT_ATTRS))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs=TEXT_ATTRS))
    
def signup_user(request):
    if(request.user.is_authenticated()):
        return HttpResponseRedirect('/users/profile')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            u = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            u.first_name = form.cleaned_data['first_name']
            u.last_name = form.cleaned_data['last_name']
            u.save()
            u = authenticate(username=form.cleaned_data['username'], 
                         password=form.cleaned_data['password'])
            login(request, u)
            return HttpResponseRedirect('/users/profile')
    else:
        form = SignUpForm()
        
    return render_to_response('users/user-signup.html', {
        'form': form
    }, context_instance=RequestContext(request))