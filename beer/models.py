from django.contrib.auth.models import User
from django.db import models
from moderation.mixins import ModerationMixin
from moderation.models import ModerationManager
from utils.mixins import TimestampMixin
from venues.models import Venue

# Beer Style model
class BeerStyle(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    # Relationships
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Beer Styles"
        ordering = ['name']
        
class BeerManager(ModerationManager):
    pass
        
# Beer model
class Beer(TimestampMixin, ModerationMixin):    
    name = models.CharField(max_length=100)
    abv = models.DecimalField(decimal_places=2,max_digits=4)
    retired = models.BooleanField(default=False)
    
    # Relationships
    style = models.ForeignKey(BeerStyle, related_name='beers')
    brewery = models.ForeignKey(Venue, related_name='beer_brewed_here')
    contributed_by = models.ForeignKey(User, related_name='contributed_beers', null=True, blank=True, on_delete=models.SET_NULL) 
    
    objects = BeerManager() 
    
    # Custom Manager
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Beer"
        ordering = ['brewery', 'name']