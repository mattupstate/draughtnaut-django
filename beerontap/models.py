from django.contrib.auth.models import User
from django.db import models
from beer.models import Beer
from venues.models import Venue
from utils.mixins import TimestampMixin

# Beer On Tap model
class BeerOnTap(TimestampMixin):
    date_removed = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(blank=True)
    
    # Relationships
    added_by = models.ForeignKey(User, related_name='beer_on_tap')
    beer = models.ForeignKey(Beer, related_name='on_tap_at')
    venue = models.ForeignKey(Venue, related_name='beer_on_tap_here')
    
    def __unicode__(self):
        return '%s - %s' % (self.beer.name, self.venue.name)
    
    class Meta:
        verbose_name_plural = "Beer on Tap"
        ordering = ['-date_created', 'venue', 'beer']
    
