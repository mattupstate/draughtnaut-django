from django.db import models
from django.contrib.auth.models import User

# Beer Style model
class BeerStyle(models.Model):
    slug = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Beer Styles"
    
# Beer model
class Beer(models.Model):    
    name = models.CharField(max_length=100)
    abv = models.DecimalField(decimal_places=2,max_digits=4)
    style = models.ForeignKey(BeerStyle)
    brewery = models.ForeignKey('venues.Venue')
    retired = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Beer"

# Beer on tap model
class BeerOnTap(models.Model):
    note = models.CharField(max_length=140)
    added_by = models.ForeignKey(User)
    beer = models.ForeignKey(Beer)
    venue = models.ForeignKey('venues.Venue')
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.beer, ': ', self.addedBy.name
    
    class Meta:
        verbose_name_plural = "Beer on Tap"