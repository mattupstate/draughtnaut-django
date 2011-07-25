from django.contrib import admin
from django.core.urlresolvers import reverse
from moderation.models import ModerationFlag

class ModerationFlagAdmin(admin.ModelAdmin):
    list_display = ['reason','content_type', 'the_object', 'date_created']
    list_filter = ['reason', 'content_type']
    
    def the_object(self, obj):
        reverse_lookup = 'admin:%s_%s_change' % (obj.content_type.app_label, obj.content_type.model)
        return '<a href="%s">%s</a>' % (
            reverse(reverse_lookup, args=(obj.object_id,)),
            obj.content_object.name,
        )
    the_object.allow_tags = True
    
admin.site.register(ModerationFlag, ModerationFlagAdmin)