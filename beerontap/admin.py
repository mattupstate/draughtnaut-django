from django.contrib import admin
from beerontap.models import BeerOnTap

class BeerOnTapAdmin(admin.ModelAdmin):
    list_display = ['venue', 'beer', 'added_by', 'date_created', 'date_removed']
    fields = ['beer', 'venue', 'comment', 'added_by', 'date_removed']
    
admin.site.register(BeerOnTap, BeerOnTapAdmin)