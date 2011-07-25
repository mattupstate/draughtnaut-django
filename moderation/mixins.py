from django.contrib.contenttypes import generic
from django.db import models
from moderation.models import ModerationFlag

class ModerationMixin(models.Model):
    approved = models.BooleanField(default=True)
    flags = generic.GenericRelation(ModerationFlag)
    
    def approve(self):
        if self.approved:
            return
        self.approved = True
        self.save()
        
    def delete(self, *args, **kwargs):
        super(ModerationMixin, self).delete(*args, **kwargs)
        self.flags.all().delete()
        
    class Meta:
        abstract = True
    
