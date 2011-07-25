from django.contrib import admin
from venues.models import Venue, VenueType

class VenueAdmin(admin.ModelAdmin):
    actions = ['batch_approve_venues']
    list_display = ['name', 'city', 'state', 'post_code', 'country', 'flag_count', 'approved']
    list_filter = ['venue_types', 'country']
    search_fields = ['name', 'city', 'state']
    fieldsets = [
        (None,  {
            'fields': ['approved', 'name', 'venue_types']
        }), 
        ('Location', {
            'fields': ['address1', 'address2', 'city', 'state', 'post_code', 'country', 'lat', 'lon']
        }), 
        ('Misc', {
            'fields': ['phone', 'website', 'notes'], 
            'classes': ['collapse']
        }), 
    ]
    
    def flag_count(self, obj):
        return obj.flags.count()
    
    def batch_approve_venues(self, request, queryset):
        queryset.update(approved=True)
        # TODO: email the contributing users
    batch_approve_venues.short_description = 'Mark selected venues as approved'

class VenueTypeAdmin(admin.ModelAdmin):
    fields = ['name']
    
admin.site.register(Venue, VenueAdmin)
admin.site.register(VenueType, VenueTypeAdmin)