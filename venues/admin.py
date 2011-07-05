from venues.models import Venue
from venues.models import VenueType
from venues.models import VenueTip
from django.contrib import admin

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'post_code', 'country')
    list_filter = ['venue_type', 'country']
    search_fields = ['name', 'city', 'state']
    fieldsets = [
        (None,  {
            'fields': ['name', 'slug', 'venue_type']
        }), 
        ('Location', {
            'fields': ['address1', 'address2', 'city', 'state', 'post_code', 'country', 'lat', 'lon']
        }), 
        ('Misc', {
            'fields': ['phone', 'website', 'notes', 'foursquare_id'], 
            'classes': ['collapse']
        }), 
    ]

class VenueTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']
    
admin.site.register(Venue, VenueAdmin)
admin.site.register(VenueType, VenueTypeAdmin)
#admin.site.register(VenueTip)