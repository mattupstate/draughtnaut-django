from beer.models import Beer, BeerOnTap, BeerStyle
from django.contrib import admin

class BeerStyleAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'description', 'parent']
    
class BeerAdmin(admin.ModelAdmin):
    fields = ['name', 'brewery', 'style', 'abv', 'retired']
    list_display = ('name', 'brewery', 'style', 'abv')
    list_filter = ['style']
    search_fields = ['name']

admin.site.register(Beer, BeerAdmin)
admin.site.register(BeerStyle, BeerStyleAdmin)
admin.site.register(BeerOnTap)
