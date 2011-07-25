from beer.models import Beer, BeerStyle
from django.contrib import admin

class BeerStyleAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'parent']
    
class BeerAdmin(admin.ModelAdmin):
    actions = ['batch_approve_beer']
    fields = ['approved', 'name', 'brewery', 'style', 'abv', 'retired']
    list_display = ['name', 'brewery', 'style', 'abv', 'flag_count', 'approved']
    list_filter = ['style','approved']
    search_fields = ['name']
    
    def flag_count(self, obj):
        return obj.flags.count()
    
    def batch_approve_beer(self, request, queryset):
        queryset.update(approved=True)
        # TODO: email the contributing users
    batch_approve_beer.short_description = 'Mark selected beer as approved'

admin.site.register(Beer, BeerAdmin)
admin.site.register(BeerStyle, BeerStyleAdmin)