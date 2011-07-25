from django import forms

# Form for a registered user to suggest a beer to be added
class ContributeBeerForm(forms.Form):
    TEXT_ATTRS = {'class':'text'}
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs=TEXT_ATTRS))
    style = forms.IntegerField(widget=forms.HiddenInput())
    style_auto = forms.CharField(label='Style', widget=forms.TextInput(attrs=TEXT_ATTRS))
    abv = forms.CharField(label='ABV', widget=forms.TextInput(attrs=TEXT_ATTRS))
    brewery = forms.IntegerField(widget=forms.HiddenInput())
    brewery_auto = forms.CharField(label='Brewery', widget=forms.TextInput(attrs=TEXT_ATTRS))