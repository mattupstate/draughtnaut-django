from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from beer.models import Beer
from venues.models import Venue

# Extra user data
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    favorite_beer = models.ForeignKey(Beer, null=True)
    favorite_venue = models.ForeignKey(Venue, null=True)
    
    def __unicode__(self):
        return 'User Profile'
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
    
