from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Custom user account model
class DraughtnautUser(models.Model):
    user = models.OneToOneField(User)

# Needed for custom user account    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        DraughtnautUser.objects.create(user=instance)
        
# Post save signal
post_save.connect(create_user_profile, sender=User)
        
