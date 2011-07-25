from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from users.models import UserProfile

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'show_profile')
    
    def show_profile(self, obj):
        return '<a href="%s">User Profile</a>' % reverse('admin:users_userprofile_change', args=(obj.profile.id,))
    show_profile.allow_tags = True
    
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite_beer', 'favorite_venue')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)