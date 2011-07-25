from django.contrib.auth.models import User
from django.db import models
from moderation.mixins import ModerationMixin
from utils.mixins import TimestampMixin

# Venue type model, generally a bar, brewery, or store
class VenueType(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Venue Types"
        ordering = ['name']

# Venue model
class Venue(ModerationMixin, TimestampMixin):
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    post_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    website = models.CharField(max_length=100, blank=True)
    notes = models.TextField(null=True, blank=True)
    lat = models.DecimalField(decimal_places=8, max_digits=11, null=True, blank=True)
    lon = models.DecimalField(decimal_places=8, max_digits=11, null=True, blank=True)
    
    # Relationships
    venue_types = models.ManyToManyField(VenueType, related_name='venues')
    contributed_by = models.ForeignKey(User, related_name='contributed_venues', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Venues'
        ordering = ['name']